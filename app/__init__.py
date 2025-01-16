from flask import Flask
from flask_mysqldb import MySQL
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

from app import routes
