from flask import Flask

app = Flask(__name__, static_folder='static')

# Configurations
app.config.from_pyfile('config.py')

from app import routes
