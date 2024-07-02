from flask import Flask,render_template,url_for,request,flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BooleanField
from wtforms.validators import DataRequired,URL
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = "2234235346554rg53243T4#"
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField("map_url",validators=[DataRequired(),URL(message="Please Enter a valid url")])
    img_url = StringField("image Address",validators=[DataRequired(),URL(message="Please Enter a valid url")])
    location = StringField('location', validators=[DataRequired()])
    seats = StringField('No. of Seats', validators=[DataRequired()])
    has_toilet = BooleanField('Does it have a toilet?')
    has_wifi = BooleanField('Does it have a Wifi?')
    has_sockets = BooleanField('Does it have a Sockets?')
    can_take_calls  = BooleanField('Do they take calls?')
    coffee_price = StringField('', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Cafe(db.Model):
	__tablename__ = "cafe"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), unique=True, nullable=False)
	map_url = db.Column(db.String(500), nullable=False)
	img_url = db.Column(db.String(500), nullable=False)
	location = db.Column(db.String(250), nullable=False)
	seats = db.Column(db.String(250), nullable=False)
	has_toilet = db.Column(db.Boolean, nullable=False)
	has_wifi = db.Column(db.Boolean, nullable=False)
	has_sockets = db.Column(db.Boolean, nullable=False)
	can_take_calls = db.Column(db.Boolean, nullable=False)
	coffee_price = db.Column(db.String(250), nullable=True)

	def to_dict(self):
		return {column.name:getattr(self,column.name) for column in self.__table__.columns}


@app.route("/")
def home():
	shops = Cafe.query.all()
	choice= ['No','Yes']
	return render_template('index.html',cafes=shops,choice=choice,int=int)


@app.route('/details/<int:id>')
def cafe_details(id):
	cafe = Cafe.query.get(id)
	return render_template('cafe.html',cafe=cafe)

@app.route('/add',methods=['GET','POST'])
def add_cafe():
	form = CafeForm()
	if form.validate_on_submit():
		cafe = Cafe(name = form.cafe.data,
			map_url = form.map_url.data,
			img_url=form.img_url.data,
			location=form.location.data,
			seats= form.seats.data,
			has_toilet=form.has_toilet.data,
			has_wifi=form.has_wifi.data,
			has_sockets=form.has_sockets.data,
			can_take_calls=form.can_take_calls.data,
			coffee_price=form.coffee_price.data)
		db.session.add(cafe)
		db.session.commit()
		return '<h1>Success</h1> <br> <a href="/">Return to home</a>'

	return render_template('add.html',form=form)


@app.route('/report-closed/<cafe_id>')
def delete(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return "Deleted"
    else:
    	return "Wrong Api Key"

if __name__ == '__main__':
	app.run(debug=True)