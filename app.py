# test2 project, app.py
# Mike Colbert 09/20/2019

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict")
def about():
    return predict.html

if __name__ == '__main__':
    app.run(debug=True, port=8000)


