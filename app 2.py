# Put your app in here.
from flask import Flask, jsonify, request
from operations import add, sub, mult, div


app = Flask(__name__)

# /add ? a=2 & b=2
@app.route('/add', methods=['GET'])
# @app.route('/math/add', methods=['GET'])
def index():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return add(a,b)

@app.route('/sub', methods=['GET'])
# @app.route('/math/sub', methods=['GET'])
def subhandler():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a,b))

@app.route('/mult', methods=['GET'])
# @app.route('/math/mult', methods=['GET'])
def multhandler():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a,b))

@app.route('/div', methods=['GET'])
# @app.route('/math/div', methods=['GET'])
def divhandler():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a,b))

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)


   