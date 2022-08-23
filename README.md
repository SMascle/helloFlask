# helloFlask
Dépot du projet orientée objet 


### Commandes de chargement de l'environement Python 3.8.6 via pyenv

##intaller Python 3.8.6
pyenv install 3.8.6


##documentation pyenv local
help pyenv local
man pyenv 
tldr pyenv

##création environement pour le projet helloFlask

pyenv virtualenv 3.8.6 helloFlask
pyenv activate helloFlask

python --version 
# affichera bien que la version de base est 3.8.6

## imposer un environement python dans le dossier courant
pyenv local 3.8.6
pyenv local testEnv310

### Fin Pyenv 


### Intallation et utilisation de Poetry

## Guide poetry
tldr poetry
poetry

## initialiser :
poetry init --no-interaction
# si vous avez des références vous pouvez démarrer avec des intéractions.

## ajouter une dépendance
poetry add ___________

## supprimer une dépendance
poetry remove ____________

## Voir et/ou modifier le statut
cat pyproject.toml
gedit pyproject.toml

## Appliquer une commande poetry
poetry run ___________

### Fin poetry



### Utiisation Flask et Jinja
# commencer avec les étapes précédentes à avoir les bonnes dépendances et environements informatiques.

## Installer Jinja2
poetry add jinja2









