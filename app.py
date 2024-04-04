# test2 project, app.py
# Mike Colbert 09/20/2019

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World"

@app.route("/flask")
def hello():
    n1 = 10
    n2 = 20
    sum = n1 + n2
    return str(sum)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


