"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


class Users(db.Model):

    __tablename__ = "users"

    

    # def full_name(self):
    #     """Return full name of user."""
    #     return f"{self.first_name} {self.last_name}"
	

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    first_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    
    last_name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    
    image_url = db.Column(db.Text,
                     nullable=True,
                     unique=True, default = DEFAULT_IMAGE_URL)
    
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
# def __repr__(self):
    #     p = self
    #     return f"<User id{p.id} first name{p.first_name} last_name{p.last_name}"

#####################################################################################################
##PART 2##

class Post(db.Model):
    __tablename__ = 'Posts'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    title = db.Column(db.Text, nullable = False)

    content = db.Column(db.Text, nullable = False)

    created_at = db.Column(db.DateTime,
        nullable=False)
    
    user_id = db.Column(db.Text, db.ForeignKey("'users.id'"), nullable = False)

def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from app import app
    connect_db(app)

    db.drop_all()
    db.create_all()