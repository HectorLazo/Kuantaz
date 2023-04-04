from . import db

class Institucion(db.Model):
    __tablename__ = 'instituciones'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    direccion = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.Date(), nullable=False)

    
    @classmethod
    def new(cls, nombre, descripcion, direccion, fecha_creacion):
        return Institucion(nombre=nombre, 
                           descripcion=descripcion, 
                           direccion=direccion, 
                           fecha_creacion=fecha_creacion)

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
        return self.nombre