"""Blogly application."""

from flask import Flask, render_template, request, redirect, flash  
from models import db, connect_db, Users, Post, Tag, Posttag
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'abc1234'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension
db = SQLAlchemy
db.app = app
connect_db(app)



@app.route('/')
def root():
    """Homepage redirects to list of users."""

    return redirect("/users")


@app.route('/users')
def home_page():
    """SHOW LIST OF ALL USERS"""
    user = Users.query.all()
    return render_template('users.html', user = user)

@app.route('/users/new', methods=["GET"])
def user_new_form():
    """Show a form to create a new user"""
    return render_template('users/new.html')

@app.route('/users/new', methods=['POST'])
def create_user():
    
    new_user = Users(
	        first_name=request.form['first_name'],
	        last_name=request.form['last_name'],
	        image_url=request.form['image_url'] or None)
    
    db.session.add(new_user)
    db.session.commit()
    return redirect(f"users")


@app.route('/users/<int:user_id>')
def users_show(user_id):
 """Show a page with info on a specific user"""
 user = Users.query.get_or_404(user_id)
 return render_template('users/show.html', user=user)

@app.route("/users/<int:users.id>/edit", methods = ["POSTS"])
def update_user():

    first_name = request.form(first_name)
    last_name = request.form(last_name)
    url = request.form(url)

    new_user = Users(first_name = first_name, last_name = last_name, url = url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f"/users/<int:users.id>")

@app.route("/users/<int:users.id>/delete", methods=["POST"])
def remove_user(user_id):
    """Removing a user"""
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")


####################################################################################################
##PART 2##  

@app.route("/users/<int:users.id>/posts/new", methods=['GET'])
def show_post_form():
    return render_template("post_form.html")


app.route("/users/<int:users.id>/post/new", methods= ['POST'])
def handle_add_form():

    title = request.form("title")
    content = request.form("content")

    new_post = Post(title = title, content = content)
    db.add(new_post)
    db.commit()

    return redirect("user.html")


@app.route("/post/<int:post.id>")
def the_post():

    return render_template("post.html")

@app.route("posts/<int:post.id>/edit", methods=["GET"])
def show_edit_form():

    return render_template("post_edit.html")

@app.route("posts/<int:post.id>/edit", methods=["POST"])
def handle_edit_form():
    title = request.form("title")
    content = request.form("content")

    post = Post(title = title, content = content)
    db.add(post)
    db.commit()

    return redirect(f"/users/{post.user_id}")

@app.route("/posts/<int:post.id>/delete", methods=["POST"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    db.session.delete(post)
    db.session.commit()

    return redirect (f"/users/{post.user_id}")

####################################################################################################
##Part 3##

@app.route("/tags", methods=['GET'])
def list_of_tags():
    return render_template('tags.html')

@app.route("/tags<int:tag.id>/", methods=['GET'])
def show_tags():
    tag = Tag.query.get_or_404()
    return render_template("tag.html", tag = tag)

@app.route("/tags/new", methods = ['GET'])
def tag_form():
    tag = Tag.query.get_or_404()
    return render_template("add_tag.html", tag = tag)

@app.route("/tags/new", methods = ['POST'])
def tag_form():
    post_id = [int(num) for num in request.form.getlist("posts")]
    posts = Post.query.filter(Post.id.in_(post_id).all())
    new_tag = Tag(name= request.form['name'], posts = posts)

    db.session.add(new_tag)
    db.session.commit()

    return render_template("/tag.html")

@app.route("/tags/<int:tag.id>/edit", methods = ['GET'])
def show_edit_tag():
    tag = Tag.query.get_or_404()
    return render_template("edit_tag.html", tag = tag)

@app.route("/tags/<int:tag.id>/edit", methods = ['POST'])
def edit_tag():
    tag = Tag.query.get_or_404(tag_id)
    tag_name = request.form("name")
    post_id = [int(num) for num in request.form.getlist("posts")]
    tag.posts = Post.query.filter(Post.id.in_(post_id)).all()   

    db.session.add(tag)
    db.session.commit()

    flash(f"Tag '{tag.name}' edited.")
    redirect('/tags')

@app.route('/tags/<int:tag_id>/delete', methods=["POST"])
def tags_destroy(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    flash(f"Tag '{tag.name}' deleted.")

    return redirect("/tags")