import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']='da951d0696484487c7d04bdeb95f6777'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db= SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'

app.config['MAIL_PORT']=587

app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='harshith7171@gmail.com'
app.config['MAIL_PASSWORD']='kuhaviojcieddzvz'

mail = Mail(app)
from flaskblog import routes 

