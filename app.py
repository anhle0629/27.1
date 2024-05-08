"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, Users
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



@app.route('/users')
def home_page():
    """SHOW LIST OF ALL USERS"""
    user = Users.query.all()
    return render_template('list.html', user = user)

@app.route('/users/new', methods=['POST'])
def create_user():
    first_name = request.form("first name")
    last_name = request.form("last name")
    url = request.form("url")

    new_user = Users(first_name = first_name, last_name = last_name, url = url)
    db.session.add(new_user)
    db.session.commit()
    return redirect(f"/new_user.id")


@app.route("/users/<int:users.id>")
def show_user():
    """SHOW DETAIL ABOUT A SINGLE USER"""
    user = Users.query.get_or_404(Users.id)
    return render_template('user_detail_page.html', user = user)

@app.route("/users/<int:users.id>/edit")
def update_user():
    first_name = request.form(first_name)
    last_name = request.form(last_name)
    url = request.form(url)

    new_user = Users(first_name = first_name, last_name = last_name, url = url)
    db.session.add(new_user)
    db.session.commit()

    return redirect(f"/users/<int:users.id>")

@app.route("/users/<int:users.id>/delete")
def remove_user():
    """Removing a user"""
    first_name = request.form(first_name)
    last_name = request.form(last_name)
    url = request.form(url)

    delete_user = Users(first_name = first_name, last_name = last_name, url = url)
    db.session.delete(delete_user)
    db.session.commit()

    return redirect("/users")
