from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Ecrit avec du codage un peu html je pense. \n Eh mais c'est la page d'accueil ! Vous avez aussi accès à la page 'about' est la page 'form'.<h1>"




@app.route("/about")
def about():
	return "<h1>Connaissez-vous ... Mouais on verra plus tard.<h1>"

@app.route("/form")
def form():
	return "<h1>Veuillez remplire ce formulaire de votre sang.<h1>"


if __name__ == '__main__':
	app.run(debug=True)



