from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

# @app.route("/about")
# def about():
#     return "<h1>About Page<h1/>"

if __name__ == '__main__':
    app.run(debug= True)