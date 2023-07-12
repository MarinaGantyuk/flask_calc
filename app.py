from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/welcome', methods=['GET'])
def index():
    return "welcome"

@app.route('/welcome/home', methods=['GET'])
def index2():
    return "welcome home"

@app.route('/welcome/back', methods=['GET'])
def index3():
    return "welcome back"

# if __name__ == '__main__':
#     app.run(debug=True)

