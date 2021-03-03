#hw: finish up routes

import flask
from flask import request

app = flask.Flask(__name__)

@app.route("/")
def index():
  return flask.render_template("index.html")

@app.route('/general', methods=["GET", "POST"])
def general():
  if requestmethod == "POST":
    content = request.json
    generalP.append(content)

  return flask.render_template('general.html', posts = generalP)

@app.route('/books', methods=["GET", "POST"])
def books():
  if requestmethod == "POST":
    content = request.json
    booksP.append(content)

  return flask.render_template('books.html', posts = booksP)

@app.route('/tv', methods=["GET", "POST"])
def tv():
  if requestmethod == "POST":
    content = request.json
    tvP.append(content)

  return flask.render_template('tv.html', posts = tvP)

@app.route('/games', methods=["GET", "POST"])
def general():
  if requestmethod == "POST":
    content = request.json
    gamesP.append(content)

  return flask.render_template('games.html', posts = gamesP)

@app.route("/about")
def about():
  return render_template('about.html')

if __name__ == "__main__":
  app.run()