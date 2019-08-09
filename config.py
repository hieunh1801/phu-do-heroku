from flask import Flask, escape, request, blueprints
from routers.admin import admin
from routers.pages import page


app = Flask(__name__)

app.register_blueprint(admin)
app.register_blueprint(page)
