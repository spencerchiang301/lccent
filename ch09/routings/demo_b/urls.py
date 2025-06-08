from flask import Blueprint

demo_b = Blueprint('demo_b',__name__, url_prefix="/demo_b")

@demo_b.route("/hello", methods=['GET'])
def hello():
    return "hello from demo B"

@demo_b.route("/ping", methods=['GET'])
def ping():
    return "pong B"