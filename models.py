from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User (db.model):
    __table__ = 'users'

    id = db.column(db.integer, primary_key = True)
    first_name = db.column(db.string)
    last_name = db.column(db.string)
    username = db.column(db.string)