from flask import Blueprint

demo_a = Blueprint('demo_a',__name__, url_prefix="/demo_a")

@demo_a.route("/hello", methods=['GET'])
def hello():
    return "hello from demo A"

@demo_a.route("/ping", methods=['GET'])
def ping():
    return "pong"