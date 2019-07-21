#!/usr/local/bin/python
# -*- coding: <encoding name> -*-

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class RegistrosForm(FlaskForm):
    nomecompleto = StringField('Nome Completo', validators=[DataRequired()])
    cpf = IntegerField('Cpf', validators=[DataRequired()])
    idade = IntegerField('Idade', validators=[DataRequired()])
    cidade = StringField('Cidade', validators=[DataRequired()])
    telefone = IntegerField('Telefone', validators=[DataRequired()])
    sobrevoce = TextAreaField('Sobre Voce', validators=[DataRequired()])
    submit = SubmitField('OK')
