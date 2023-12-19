from flask import Flask, render_template
import requests
from blog import Blog

blogs_data = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
all_blogs = []
for blog in blogs_data:
    blog_obj = Blog(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    all_blogs.append(blog_obj)

app = Flask(__name__)

@app.route('/')
def get_blogs():
    return render_template("index.html", blogs=all_blogs)

@app.route('/<id>')
def show_post(id):
    current_blog = None
    for blog in all_blogs:
        if blog.id == int(id):
            current_blog = blog
    return render_template("post.html", blog=current_blog)

if __name__ == "__main__":
    app.run(debug=True)
