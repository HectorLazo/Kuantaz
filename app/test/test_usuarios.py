import json
import unittest
import datetime
from config import config
from app import db
from app import create_app
from app.models.usuario import Usuario

class TestUsuarioAPI(unittest.TestCase):
    def setUp(self):

        self.usuario1_data = {
                'nombre': 'Juan',
                'apellidos': 'Perez',
                'rut': '12345678-9',
                'fecha_nacimiento': '1990-01-01',
                'cargo': 'Gerente',
                'edad': 30
            }
        self.usuario2_data = {
                'nombre': 'Pedro',
                'apellidos': 'Alvi',
                'rut': '13245678-9',
                'fecha_nacimiento': '1991-01-01',
                'cargo': 'Operador',
                'edad': 33
            }
        self.usuario_update_data = {
                'nombre': 'Juan',
                'apellidos': 'Pérez',
                'rut': '12345678-9',
                'fecha_nacimiento': '1990-01-01',
                'cargo': 'Gerente',
                'edad': 33
            }


        environment = config['test']
        self.app = create_app(environment)
        self.client = self.app.test_client()
        self.content_type = 'application/json'
        self.path = 'http://127.0.0.1:5000/usuarios'
    
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_get_all_usuarios(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

    def test_create_usuario(self):

        response = self.client.post(path=self.path, 
                                    data=json.dumps(self.usuario1_data), 
                                    content_type=self.content_type)
        
        response = self.client.post('/usuarios', json=self.usuario1_data)

        print("CODIGO: ",response.status_code)

        # Comprueba que el usuario fue creado con éxito
        self.assertEqual(response.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()