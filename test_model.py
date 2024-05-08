from unittest import TestCase

from app import app
from models import db, Users

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_intro_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserTestModel(TestCase):

    __tablename__ = "users"

    def setUp(self):
        """clear up any existing user"""
        Users.query.delete()
    
    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def add_user(sef):
        user = Users(first_name = 'Anh', last_name = "Le")

        db.session.add(user)
        db.session.commit

        first_name = Users.get_by_first_name("Anh")
        self.assertEqual(first_name)
    
    def remove_user(self):
        delete_user = Users(first_name = 'Anh', last_name = "Le")

        db.session.remove(delete_user)
        db.session.commit

        first_name = Users.get_by_first_name("Anh")
        self.assertEqual(first_name)