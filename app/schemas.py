from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class UsuarioSchema(Schema):
    class Meta:
        fields= ('id', 'nombre', 'apellidos', 'rut', 'fecha_nacimiento', 'cargo', 'edad')


class ParamUsuarioSchema(Schema):
    nombre = fields.Str(required=True, validate=Length(max=30))
    apellidos = fields.Str(required=True, validate=Length(max=50))
    rut = fields.Str(required=True, validate=Length(min=7,max=9))
    fecha_nacimiento = fields.Date(required=True)
    cargo = fields.Str(required=True, validate=Length(max=50))
    edad = fields.Int(required=True)


class InstitucionSchema(Schema):
    class Meta:
        fields= ('id', 'nombre', 'descripcion', 'direccion', 'fecha_creacion')


class ParamInstitucionSchema(Schema):
    nombre = fields.Str(required=True, validate=Length(max=50))
    descripcion = fields.Str(required=True)
    direccion = fields.Str(required=True)
    fecha_creacion = fields.Date(required=True)


class ProyectoSchema(Schema):
    class Meta:
        fields= ('id', 'nombre', 'descripcion', 'fecha_inicio', 'fecha_termino', 'responsable_id', 'institucion_id')


class ParamProyectoSchema(Schema):
    nombre = fields.Str(required=True, validate=Length(max=50))
    descripcion = fields.Str(required=True)
    fecha_inicio = fields.Date(required=True)
    fecha_termino = fields.Date(required=True)
    responsable_id = fields.Integer(required=True)
    institucion_id = fields.Integer(required=True)

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
param_usuarios_schema = ParamUsuarioSchema()

institucion_schema = InstitucionSchema()
instituciones_schema = InstitucionSchema(many=True)
param_instituciones_schema = ParamInstitucionSchema()

proyecto_schema = ProyectoSchema()
proyectos_schema = ProyectoSchema(many=True)
param_proyectos_schema = ParamProyectoSchema()