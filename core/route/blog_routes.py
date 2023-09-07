from flask import Blueprint, render_template

from core.models import Blog


blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/blogs")
def blogs():
    blogs = Blog.query.all()
    return render_template("index.html", blogs=blogs)


@blog_bp.route("/blog")
def blog_home():
    return "Blog Home Page"
