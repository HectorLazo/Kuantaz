from . import db

from sqlalchemy.event import listen

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    rut = db.Column(db.String(9), nullable=False)
    fecha_nacimiento = db.Column(db.Date(), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)

    @classmethod
    def new(cls, nombre, apellidos, rut, fecha_nacimiento, cargo, edad):
        return Usuario(nombre=nombre, apellidos=apellidos, rut=rut, fecha_nacimiento=fecha_nacimiento, cargo=cargo, edad=edad)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False
        
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False
    
    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
