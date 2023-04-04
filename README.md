# Kuantaz
Prueba Técnica para Kuantaz

La APi Rest debe tener las siguientes características:

Desarrolle la Api Rest con Flask https://flask.palletsprojects.com/en/2.2.x/
Usar Base de datos Postgresql.
Debes crear un CRUD para Instituciones
Crear servicios para listar instituciones,proyectos y usuarios.
    [GET].../instituciones
    [GET].../proyectos
    [GET].../usuarios
Crear servicio para listar una institución (Filtró por id) con sus respectivos proyectos y responsable del proyecto.
    [GET].../instituciones/detalle/<id>
Crear servicio para listar un usuario (filtro por Rut) con sus respectivos proyectos.
    [GET].../usuarios/rut/<rut>
Crear servicio para listar instituciones donde a cada institución se agregue a la dirección la ubicación de google maps ejemplo: “https://www.google.com/maps/search/+ direccion ” y la abreviación del nombre (solo los primeros tres caracteres).
    [GET].../instituciones/direcciones
Crear servicio para listar los proyectos que la respuesta sea el nombre del proyecto y los días que faltan para su término. 
    [GET].../proyectos/restante


Suma Puntos si:

Crear documentación con Swagger.
    127.0.0.1:500/api/docs

Crear archivo Postman u otro.
    Kuantaz.postman_collection.json
Ocupa ORM de preferencia sqlalchemy.
    /app/models
Test unitarios
    Se realizaron parcialmente algunos de Usuarios
