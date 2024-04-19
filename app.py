from flask import Flask, jsonify, request

app = Flask(__name__)

from api import bp
app.register_blueprint(bp)