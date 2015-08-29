from app import app, login_manager
from app.forms import SignupForm, LoginForm, EventForm
from datetime import datetime
from flask import render_template, request, redirect, url_for
from models import User, Event
from flask.ext.login import login_user, logout_user, login_required


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('signup'))

@login_manager.user_loader
def load_user(userid):
	return User.query.get(userid)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		new_user = User(first_name=form.first_name.data,
			last_name=form.last_name.data,
			place=form.place.data,
			email=form.email.data,
			password=form.password.data)
	 	new_user.save()
	 	login_user(new_user, remember=True)
		return redirect('/')
	return render_template('signup.html', form=form)
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		login_user(user, remember=True)
		return redirect(url_for('index'))
	return render_template ('login.html', form=form)


@app.route ('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
	form = EventForm()
	if form.validate_on_submit():
		new_event = Event(title=form.title.data,
			description=form.description.data,
			image_url=form.image_url.data,
			category=form.category.data,
			place=form.place.data)
		new_event.save()
		return redirect(url_for('show_event', id=new_event.id))
	return render_template('create_event.html', form=form)

@app.route('/events/<int:id>')
def show_event(id):
	event = Event.query.get(id)
	return render_template('event.html', event=event)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
