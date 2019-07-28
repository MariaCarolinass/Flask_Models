from app import app

from flask import render_template, flash, redirect, url_for, request

from app.forms import RegistrosForm

from app import db
from app.models import Model


@app.route('/')

@app.route('/index', methods=['GET','POST'])
def index():
    hellow={'saudacao':'Hellow, Word'}
    return render_template('index.html', titulo='Home', hellow=hellow)

@app.route('/registros', methods=['GET','POST'])
def registros():
    form = RegistrosForm()
    if form.validate_on_submit():
        model = Model(nomecompleto=form.nomecompleto.data, cpf=form.cpf.data,
                    idade=form.idade.data, cidade=form.cidade.data,
                    telefone=form.telefone.data, sobrevoce=form.sobrevoce.data)
        db.session.add(model)
        db.session.commit()
        return redirect(url_for("lista"))
        flash("Formulário Ok")
    return render_template('registros.html', titulo='Registro', form=form)

@app.route('/cadastrado', methods=['GET','POST'])
def cadastrado():
    if request.method == 'POST':
        try:
            nomecompleto = request.form['nomecompleto']
            cpf = request.form['cpf']
            idade = request.form['idade']
            cidade = request.form['cidade']
            telefone = request.form['telefone']
            sobrevoce = request.form['sobrevoce']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO registros (nomecompleto, cpf, idade, cidade, telefone, sobrevoce) VALUES (?,?,?,?,?,?)"
                    ", (nomecompleto, cpf, idade, cidade, telefone, sobrevoce)" )
                con.commit()
                msg = "Registros Adicionados com Sucesso"
        except:
            con.rollback()
            msg = "Erro ao Inserir Registros"
        finally:
            return render_template('cadastrado.html', titulo='Cadastrado', msg=msg)
            con.close()
import mysql.connector
@app.route('/lista')
def lista():
   con = sql.connect("app.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from registros")
   rows = cur.fetchall();
   return render_template("lista.html",rows = rows)
