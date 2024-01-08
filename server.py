from flask import Flask, render_template
import requests

app = Flask(__name__)

url_blogs = 'https://api.npoint.io/b8fb46730f57568d6b43'
blog_data = requests.get(url_blogs).json()


@app.route("/")
def index():
    return render_template('index.html', blogs=blog_data)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
