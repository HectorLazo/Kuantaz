from . import db

class Proyecto(db.Model):
    __tablename__ = 'proyectos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_inicio = db.Column(db.Date(), nullable=False)
    fecha_termino = db.Column(db.Date(), nullable=False)
    responsable_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    responsable = db.relationship('Usuario', backref='proyectos')
    institucion_id = db.Column(db.Integer, db.ForeignKey('instituciones.id'), nullable=False)
    institucion = db.relationship('Institucion', backref='proyectos')

    @classmethod
    def new(cls, nombre, descripcion, fecha_inicio, fecha_termino, responsable_id, institucion_id):
        return Proyecto(nombre=nombre, 
                        descripcion=descripcion, 
                        fecha_inicio=fecha_inicio, 
                        fecha_termino=fecha_termino,
                        responsable_id=responsable_id,
                        institucion_id=institucion_id)

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
