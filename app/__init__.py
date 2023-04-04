from flask import Flask

from .models import db
from .models.usuario import Usuario
from .models.proyecto import Proyecto
from .models.institucion import Institucion

from .apis.usuario_service import usuario_endpoint
from .apis.institucion_service import institucion_endpoint
from .apis.proyecto_service import proyecto_endpoint

from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger config
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  
    API_URL,
    config={ 
        'app_name': "Test Application"
    }
)

def create_app(environment):

    app.config.from_object(environment)
    app.register_blueprint(swaggerui_blueprint)
    app.register_blueprint(usuario_endpoint)
    app.register_blueprint(institucion_endpoint)
    app.register_blueprint(proyecto_endpoint)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app