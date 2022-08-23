from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html", title='Menu')




@app.route("/about")
def about():
	return render_template("about.html", title='about')

@app.route("/form")
def form():
	return render_template("form.html", title='form')


if __name__ == '__main__':
	app.run(debug=True)



