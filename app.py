from flask import Flask, render_template, url_for, request

app = Flask(__name__)


liste_noms = []


@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", title='Menu')




@app.route("/about")
def about():
	return render_template("about.html", title='about')

@app.route("/form", methods=["POST", "GET"])
def form():
	if request.method == "POST":
		liste_noms.append(request.form['nm'])
		print(liste_noms)
		return render_template("form.html", title='form', liste_noms=liste_noms)
	else:
		return render_template("form.html", title='form', liste_noms=liste_noms)


if __name__ == '__main__':
	app.run(debug=True)



