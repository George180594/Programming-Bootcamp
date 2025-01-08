from flask import Flask,render_template


app=Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/user")
def user():
    return render_template("george.html")

if __name__=="__main__":
    app.run(debug=True)