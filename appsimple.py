from flask import Flask   # import de l'objet Flask

app = Flask(__name__)     # instantiation de l'application, et on prit pour que plusieurs personnes n'ait pas le même prénom.

@app.route("/")    #association d'une route(URL) avec ...
def home():       #... la fonction home()
   return "<p>Bienvenue chez moi<p>"   # on renvoie une chaîne de caractère irréaliste.


def hello():
	return "<p>Je vous aime.<p>"


app.run()     #démarrage de l'application

   
