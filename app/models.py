from app import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomecompleto = db.Column(db.String(50), index=True)
    cpf = db.Column(db.Integer, index=True)
    idade = db.Column(db.Integer, index=True)
    cidade = db.Column(db.String(50), index=True)
    telefone = db.Column(db.Integer, index=True)
    sobrevoce = db.Column(db.String(200), index=True)


    def __repr__(self):
        return '<Model {}>'.format(self.nomecompleto, self.cpf, self.idade,
         self.cidade, self.telefone, self.sobrevoce)
