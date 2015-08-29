from app import db
from flask.ext.login import UserMixin

class Place(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)

class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String)
	last_name = db.Column(db.String)
	place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
	place = db.relationship('Place')
	email = db.Column(db.String)
	image_url = db.Column(db.String)
	password = db.Column(db.String)

	def save(self):
		db.session.add(self)
		db.session.commit()
	

class Event(db.Model):
	id = db.Column (db.Integer, primary_key=True)
	title = db.Column(db.String)
	description = db.Column(db.Text)
	image_url = db.Column(db.String)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	user = db.relationship('User')
	place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
	place = db.relationship('Place')
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	category = db.relationship('Category')

	def save(self):
		db.session.add(self)
		db.session.commit()


class Attendance(db.Model):
	id = db.Column (db.Integer, primary_key=True)
	first_name = db.Column(db.String)
	last_name = db.Column(db.String)
	email = db.Column (db.String)
	phone_number = db.Column (db.String)
	event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
	event = db.relationship('Event')

