from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from time import sleep

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), unique=False, nullable=False)
	year = db.Column(db.Integer(), unique=False, nullable=False)
	description =  db.Column(db.String(120), unique=False, nullable=False)
	rating =  db.Column(db.Float(120), unique=False, nullable=False)
	ranking =  db.Column(db.Integer(), unique=False, nullable=False)
	review =  db.Column(db.String(120), unique=False, nullable=False)
	img_url =  db.Column(db.String(120), unique=False, nullable=False)

	def __repr__(self):
		return f'<Movie {self.title}>'
	
db.create_all()
class EditForm(FlaskForm):
	rating = StringField('Rating',validators=[DataRequired()])
	review = StringField('Review',validators=[DataRequired()])
	submit = SubmitField('Submit')

class AddMovie(FlaskForm):
	title = StringField("Movie Title",validators=[DataRequired()])
	submit = SubmitField("Add Movie")


@app.route("/")
def home():
	all_movies = Movie.query.order_by(Movie.rating).all()

	for i in range(len(all_movies)):
		all_movies[i].ranking = len(all_movies) - i
	
	print(all_movies)
	return render_template("index.html",movies = all_movies)

@app.route("/add",methods=["GET","POST"])
def add():
	form = AddMovie()
	if form.validate_on_submit():
		api_key = "b80bd02b228a5d3b687019164ba7f3a6"
		parameter = {
		'api_key':api_key,
		'query' : form.title.data
		}
		response = requests.get("https://api.themoviedb.org/3/search/movie",params=parameter)
		data = response.json()['results']
		return render_template("select.html",options = data)
	
	return render_template("add.html",form = form)
	

@app.route("/update/<int:id_>",methods = ["GET","POST"])
def update(id_):
	form = EditForm()
	if form.validate_on_submit():
		book_to_update = Movie.query.get(id_)
		book_to_update.rating = float(form.rating.data) 
		book_to_update.review = form.review.data
		db.session.commit()
		return redirect("/")  

	return render_template('edit.html',form = form)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
	book_to_delete = Movie.query.get(movie_id)
	db.session.delete(book_to_delete)
	db.session.commit()
	return redirect(url_for("home"))

@app.route("/find/<movie_id>")
def find(movie_id):
	MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
	movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
	response = requests.get(movie_api_url,params={'api_key':"b80bd02b228a5d3b687019164ba7f3a6","language": "en-US"})
	data = response.json()
	new_movie = Movie(
		title = data['title'],
		year=data['release_date'].split("-")[0],
		img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
		description=data["overview"],rating=3.4,ranking=0,review='A movie'
		)
	db.session.add(new_movie)
	db.session.commit()
	sleep(2)
	return redirect(f"/update/{new_movie.id}")
	



if __name__ == '__main__':
    app.run(debug=True)
