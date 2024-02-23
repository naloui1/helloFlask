import sqlite3

# Création de la base de donnée
#newfile : écrire le nom de BD et mettre .db

# Création de la connexion à la base dedonnée
con =sqlite3.connect('base.db')  # base.db créé par vscode


mycursor = con.cursor()

mycursor.execute("CREATE TABLE compteur (visite int)")