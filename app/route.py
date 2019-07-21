from app import app

from flask import render_template

from app.forms import RegistrosForm

@app.route('/')

@app.route('/index')

def index():

    nome={'seunome':'Carol'}

    return render_template('index.html', titulo='Home', nome=nome)

@app.route('/registros')

def registros():

    form = RegistrosForm()

    return render_template('registros.html', titulo='Registro', form=form)
