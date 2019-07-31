from app import app

from flask import render_template, flash, redirect, url_for, request

from app.forms import RegistrosForm

from app import db
from app.models import Model

import sqlite3

import mysql.connector

@app.route('/')

@app.route('/index', methods=['GET','POST'])
def index():
    hellow={'saudacao':'Hellow, Word'}
    return render_template('index.html', titulo='Home', hellow=hellow)

@app.route('/registros', methods=['GET','POST'])
def registros():
    form = RegistrosForm()
    db = mysql.connector.connect(host="localhost", user="root", passwd="carol", database="Model")

    if form.validate_on_submit():
        model = Model(nomecompleto=form.nomecompleto.data, cpf=form.cpf.data,
                    idade=form.idade.data, cidade=form.cidade.data,
                    telefone=form.telefone.data, sobrevoce=form.sobrevoce.data)

        nomecompleto = request.form['nomecompleto']
        cpf = request.form['cpf']
        idade = request.form['idade']
        cidade = request.form['cidade']
        telefone = request.form['telefone']
        sobrevoce = request.form['sobrevoce']

        con = mysql.connector.connect("app.db")
        cur = db.cursor()

        cur.execute("INSERT INTO registros (nomecompleto, cpf, idade, cidade, telefone, sobrevoce) VALUES (?,?,?,?,?,?)"
            ", (nomecompleto, cpf, idade, cidade, telefone, sobrevoce)" )

        return redirect(url_for("lista"))
        flash("Tudo Ok")

        db.commit()
        db.close()

    return render_template('registros.html', titulo='Registro', form=form)


@app.route('/lista')
def lista():
    db = mysql.connector.connect(host="localhost", user="root", passwd="carol", database="Model")
    con = mysql.connector.connect("app.db")
    con.row_factory = sql.Row
    cur = db.cursor()
    cur.execute("SELECT * FROM registros")
    rows = cur.fetchall();
    return render_template("lista.html",rows = rows)
