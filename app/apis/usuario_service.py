from flask import request
from flask import Blueprint

from app.models.usuario import Usuario

from .responses import response, not_found, bad_request

from app.schemas import usuario_schema, usuarios_schema, param_usuarios_schema

usuario_endpoint = Blueprint('usuario', __name__)

def set_usuario(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        usuario = Usuario.query.filter_by(id=id).first()

        if usuario is None:
            return not_found()
        
        return function(usuario)
    wrap.__name__ = function.__name__

    return wrap


@usuario_endpoint.route('/usuarios', methods=['GET'])
def get_usuarios():

    usuarios = Usuario.query.all()

    return response(usuarios_schema.dump(usuarios))


@usuario_endpoint.route('/usuarios/<id>', methods=['GET'])
@set_usuario
def get_usuario(usuario):

    return response(usuario_schema.dump(usuario))

@usuario_endpoint.route('/usuarios/rut/<rut>', methods=['GET'])
def get_usuario_rut(rut):
 
    usuario = Usuario.query.filter_by(rut=rut).first()

    if usuario is None:
        return not_found('Usuario no encontrado')

    proyectos = [{
        'id': proyecto.id, 
        'nombre': proyecto.nombre, 
        'descripcion': proyecto.descripcion,
        'fecha_inicio': str(proyecto.fecha_inicio),
        'fecha_termino': str(proyecto.fecha_termino),
        'institucion': str(proyecto.institucion)
        } for proyecto in usuario.proyectos]

    datos_usuario = {
        'id': usuario.id,
        'nombre': usuario.nombre,
        'apellidos': usuario.apellidos,
        'rut': usuario.rut,
        'fecha_nacimiento': usuario.fecha_nacimiento,
        'cargo': usuario.cargo,
        'edad': usuario.edad,
        'proyectos': proyectos
        }

    return response(datos_usuario)


@usuario_endpoint.route('/usuarios', methods=['POST'])
def create_usuario():
    json = request.get_json(force=True)

    error = param_usuarios_schema.validate(json)
    if error:
        return bad_request(error)
    
    
    usuario = Usuario.new(json['nombre'],json['apellidos'],json['rut'],json['fecha_nacimiento'],json['cargo'],json['edad'])

    if usuario.save():
        return response(usuario_schema.dump(usuario))
    
    return bad_request()


@usuario_endpoint.route('/usuarios/<id>', methods=['PUT'])
@set_usuario
def update_usuario(usuario):

    json = request.get_json(force=True)

    usuario.nombre = json.get('nombre', usuario.nombre)
    usuario.apellidos = json.get('apellidos', usuario.apellidos)
    usuario.rut = json.get('rut', usuario.rut)
    usuario.fecha_nacimiento = json.get('fecha_nacimiento', usuario.fecha_nacimiento)
    usuario.cargo = json.get('cargo', usuario.cargo)
    usuario.edad = json.get('edad', usuario.edad)

    if usuario.save():
        return response(usuario_schema.dump(usuario))
    
    return bad_request()

@usuario_endpoint.route('/usuarios/<id>', methods=['DELETE'])
@set_usuario
def delete_usuario(usuario):

    if usuario.delete():
        return response(usuario_schema.dump(usuario))
    
    return bad_request()