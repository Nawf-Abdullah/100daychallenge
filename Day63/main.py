from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-bo-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating =  db.Column(db.Float(120), unique=False, nullable=False)

    def __repr__(self):
    	return f'<Book {self.title}>'


db.create_all()
new_book = Book(title="Harry", author="Rowing", rating=9.3)
db.session.add(new_book)
db.session.commit()

all_books = []


@app.route('/')
def home():
	all_books = db.session.query(Book).all()
	print(all_books)
	return render_template('index.html',books=all_books)


@app.route("/add",methods = ["GET","POST"])
def add():
	if request.method == "POST":
		new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
		db.session.add(new_book)
		db.session.commit()
		return redirect('/')
	return render_template('add.html')



if __name__ == "__main__":
    app.run(debug=True)

