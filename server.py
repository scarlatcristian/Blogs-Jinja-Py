from flask import Flask, render_template, request
import requests
import smtplib
import os

my_email = os.environ("EMAIL")
my_password = os.environ("EMAIL_PASSWORD")


app = Flask(__name__)

url_blogs = 'https://api.npoint.io/b8fb46730f57568d6b43'
blog_data = requests.get(url_blogs).json()


@app.route("/")
def index():
    return render_template('index.html', blogs=blog_data)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = {}
        data['name'] = request.form['name']
        data['email'] = request.form['email']
        data['phone_num'] = request.form['phone_num']
        data['text'] = request.form['text']

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"Subject: Form submission\n\n{data['name'].title()} has send you and email\n\nPhone number: {data['phone_num']}\n\nEmail: {data['email']}\n\n{data['text']}")

        return render_template("contact.html", message=True)
    return render_template('contact.html', message=False)


@app.route("/sample")
def sample():
    return render_template('sample.html')


@app.route('/<id>')
def show_post(id):
    current_blog = None
    for blog in blog_data:
        if blog["id"] == int(id):
            current_blog = blog
    return render_template("post.html", blog=current_blog)


if __name__ == '__main__':
    app.run(debug=True)
