from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return "При добавлении записи произошла ошибка"

    else:
        return render_template("create_article.html")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Web_Dev')
def Web_Dev():
    return render_template("Section_Site/Web_Dev.html")


@app.route('/JavaScript')
def JavaScript():
    return render_template("Section_Site/JavaScript.html")


@app.route('/Python')
def Python():
    return render_template("Section_Site/Python.html")


@app.route('/PHP')
def PHP():
    return render_template("Section_Site/PHP.html")

@app.route('/GitHub')
def GitHub():
    return render_template("Section_Site/GitHub.html")


@app.route('/Hack')
def Hack():
    return render_template("Section_Site/Hack.html")


@app.route('/Termux')
def Termux():
    return render_template("Section_Site/Termux.html")


if __name__ == '__main__':
    app.run(debug=True)
