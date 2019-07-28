import os
import sqlite3

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'voce-nunca-sabera'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    conn = sqlite3.connect('app.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE registros (nomecompleto TEXT, cpf TEXT, idade TEXT, cidade TEXT, '
                      'telefone TEXT, sobrevoce TEXT)')
    print ("Table created successfully")
    conn.close()
