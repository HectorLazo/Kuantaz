from flask import request
from flask import Blueprint
from datetime import datetime

from app.models.proyecto import Proyecto

from .responses import response, not_found, bad_request

from app.schemas import proyecto_schema, proyectos_schema, param_proyectos_schema

proyecto_endpoint = Blueprint('proyecto', __name__)

def set_proyecto(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        proyecto = Proyecto.query.filter_by(id=id).first()

        if proyecto is None:
            return not_found('Proyecto no encontrado')
        
        return function(proyecto)
    wrap.__name__ = function.__name__

    return wrap

@proyecto_endpoint.route('/proyectos', methods=['GET'])
def get_proyectos():

    proyectos = Proyecto.query.all()

    return response(proyectos_schema.dump(proyectos))


@proyecto_endpoint.route('/proyectos/restante', methods=['GET'])
def get_proyectos_restante():

    list_proyectos = []
    proyectos = Proyecto.query.all()

    if proyectos:
        for proyecto in proyectos:
    
            dias = proyecto.fecha_termino - datetime.today().date()
            list_proyectos.append({'nombre': proyecto.nombre,
                                   'dias_restantes': dias.days})

    else:
        return not_found()

    return response(list_proyectos)


@proyecto_endpoint.route('/proyectos/<id>', methods=['GET'])
@set_proyecto
def get_proyecto(proyecto):

    return response(proyecto_schema.dump(proyecto))


@proyecto_endpoint.route('/proyectos', methods=['POST'])
def create_proyecto():
    json = request.get_json(force=True)

    error = param_proyectos_schema.validate(json)
    if error:
        return bad_request(error)
    
    proyecto = Proyecto.new(json['nombre'],
                               json['descripcion'],
                               json['fecha_inicio'],
                               json['fecha_termino'], 
                               json['responsable_id'], 
                               json['institucion_id'])

    if proyecto.save():
        return response(proyecto_schema.dump(proyecto))
    
    return bad_request()
