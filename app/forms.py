from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, PasswordField, SubmitField, StringField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, EqualTo

from models import Place, Category, User
from wtforms.widgets import TextArea



def get_all_locations():
	return Place.query.all()

def category_list():
	return Category.query.all()

class SignupForm(Form):
	first_name = TextField("Nume", [Required()])
	last_name = TextField("Prenume", [Required()])
	place = QuerySelectField("Localitatea ",[Required()], query_factory=get_all_locations, get_label="name")
	email = EmailField("Adresa email",[Required()])
	password = PasswordField("Parola",[Required()]) 
	password_confirmation = PasswordField("Confirma parola",[Required(), EqualTo('password')])
	submit = SubmitField("Trimite")

class LoginForm(Form):
	email = EmailField('Adresa email',[Required()])
	password = PasswordField('Parola',[Required()])
	submit = SubmitField('Login')

	def validate(self):
		if not Form.validate(self):
			return False
		user = User.query.filter_by(email=self.email.data).first()
		if user is None:
			self.email.errors.append('Nu exista utilizator cu asa email %s' % self.email.data)
			return False
		if user.password != self.password.data:
			self.password.errors.append('Parola este incorecta')
			return False
		return True

class EventForm(Form):
	title = TextField("Denumirea evenimentului")
	description = StringField("Detalii despre eveniment !", widget=TextArea())
	image_url = TextField(" Adresa imaginei ")
	category = QuerySelectField("Categoria evenimentului", query_factory=category_list, get_label="name")
	place = QuerySelectField("Regiunea/localitatea desfasurarii evenimentului", query_factory=get_all_locations, get_label="name")
	submit= SubmitField ('Creeaza eveniment')

