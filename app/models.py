from app import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomecompleto = db.Column(db.String(50))
    cpf = db.Column(db.Integer)
    idade = db.Column(db.Integer)
    cidade = db.Column(db.String(50))
    telefone = db.Column(db.Integer)
    sobrevoce = db.Column(db.Text(200))

    def __repr__(self):
         return '<Model %r>' % self.nomecompleto

    
