from flask import request
from flask import Blueprint

from app.models.institucion import Institucion

from .responses import response, not_found, bad_request

from app.schemas import institucion_schema, instituciones_schema, param_instituciones_schema

institucion_endpoint = Blueprint('institucion', __name__)

def set_institucion(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        institucion = Institucion.query.filter_by(id=id).first()

        if institucion is None:
            return not_found('Institucion no encontrada')
        
        return function(institucion)
    wrap.__name__ = function.__name__

    return wrap


@institucion_endpoint.route('/instituciones', methods=['GET'])
def get_instituciones():

    instituciones = Institucion.query.all()

    return response(instituciones_schema.dump(instituciones))


@institucion_endpoint.route('/instituciones/<id>', methods=['GET'])
@set_institucion
def get_institucion(institucion):

    return response(institucion_schema.dump(institucion))


@institucion_endpoint.route('/instituciones', methods=['POST'])
def create_institucion():
    json = request.get_json(force=True)

    error = param_instituciones_schema.validate(json)
    if error:
        return bad_request(error)
    
    
    institucion = Institucion.new(json['nombre'],json['descripcion'],json['direccion'],json['fecha_creacion'])

    if institucion.save():
        return response(institucion_schema.dump(institucion))
    
    return bad_request()


@institucion_endpoint.route('/instituciones/<id>', methods=['PUT'])
@set_institucion
def update_institucion(institucion):

    json = request.get_json(force=True)

    institucion.nombre = json.get('nombre', institucion.nombre)
    institucion.descripcion = json.get('descripcion', institucion.descripcion)
    institucion.direccion = json.get('direccion', institucion.direccion)
    institucion.fecha_creacion = json.get('fecha_creacion', institucion.fecha_creacion)

    if institucion.save():
        return response(institucion_schema.dump(institucion))
    
    return bad_request()

@institucion_endpoint.route('/instituciones/<id>', methods=['DELETE'])
@set_institucion
def delete_institucion(institucion):

    if institucion.delete():
        return response(institucion_schema.dump(institucion))
    
    return bad_request()

@institucion_endpoint.route('/instituciones/detalle/<id>', methods=['GET'])
@set_institucion
def get_institucion_detalle(institucion):
 
    proyectos = [{
        'id': proyecto.id, 
        'nombre': proyecto.nombre, 
        'descripcion': proyecto.descripcion,
        'fecha_inicio': str(proyecto.fecha_inicio),
        'fecha_termino': str(proyecto.fecha_termino),
        'responsable': str(proyecto.responsable)
        } for proyecto in institucion.proyectos]

    datos_institucion = {
        'id': institucion.id,
        'nombre': institucion.nombre,
        'descripcion': institucion.descripcion,
        'direccion': institucion.direccion,
        'fecha_creacion': str(institucion.fecha_creacion),
        'proyectos': proyectos
        }

    return response(datos_institucion)

@institucion_endpoint.route('/instituciones/direcciones', methods=['GET'])
def get_instituciones_direccion():
    google = 'https://www.google.com/maps/search/'

    instituciones = Institucion.query.all()

    datos_instituciones = [{
        'id': institucion.id,
        'nombre': institucion.nombre,
        'descripcion': institucion.descripcion,
        'direccion': f'{google}{institucion.direccion}{institucion.nombre[:3]}',
        'fecha_creacion': str(institucion.fecha_creacion),
        } for institucion in instituciones]

    return response(datos_instituciones)
