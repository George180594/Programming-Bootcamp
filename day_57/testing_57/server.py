from flask import Flask, render_template
import random
import datetime
import requests
app= Flask(__name__)

@app.route('/')
def home():
    random_number=random.randint(1,10)
    current_year= datetime.datetime.now().year
    return render_template("index.html",num=random_number, year=current_year)

@app.route("/guess/<user_name>")
def guess(user_name):
    # requests - gender
    gender_url = f"https://api.genderize.io?name={user_name}"
    gender_response= requests.get(gender_url)
    gender_data= gender_response.json()
    gender=gender_data["gender"]


    # requests- age
    age_url = f"https://api.agify.io/?name={user_name}"
    age_response= requests.get(age_url)
    age_data= age_response.json()
    age=age_data["age"]

    return render_template("guess.html",user_name=user_name,age=age, gender=gender)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    blog_response= requests.get(blog_url)
    all_posts=blog_response.json()
    return render_template("blog.html", posts=all_posts)

if __name__=="__main__":
    app.run(debug=True)
