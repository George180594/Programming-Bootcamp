from flask import Flask,render_template






#########################################################################
app = Flask(__name__)

@app.route("/")
def homepage():

    return render_template("index.html")
    

@app.route("/user/<name>/<int:number>")
def greet(name,number):
    return f'hello {name}, you are {number} years old'






if __name__=="__main__":
    app.run(debug=True)