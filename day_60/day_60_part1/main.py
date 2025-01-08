from flask import Flask, render_template, request,redirect, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    name=request.form['username']
    password=request.form['password']
    # return f"<h1>Name:{name}, password:{password}"
    return render_template("login.html",value_name=name,value_password=password)
    


if __name__ == "__main__":
    app.run(debug=True)
