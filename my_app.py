from flask import Flask, render_template
import sqlite3
app = Flask(__name__)                        # instantiation application


def init_db():
   
    # Se connecter à la base de données
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Créer la table si elle n'existe pas déjà
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS compteur (
            visite INT
        )
    ''')

    # Vérifier si la table est vide
    cursor.execute('SELECT COUNT(*) FROM compteur')
    row = cursor.fetchone()
    if row[0] == 0:
        # Si la table est vide, initialiser le compteur à 0
        cursor.execute('INSERT INTO compteur (visite) VALUES (0)')
        conn.commit()

    # Fermer la connexion
    cursor.close()

def incrementer_compteur():
  
    # Se connecter à la base de données
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    # Incrémenter le compteur de 1
    cursor.execute('UPDATE compteur SET visite = visite + 1')
    conn.commit()

    # Récupérer la valeur actuelle du compteur
    cursor.execute('SELECT visite FROM compteur')
    row = cursor.fetchone()
    count = row[0]

    # Fermer la connexion
    cursor.close()

    return count
# Appeler la fonction d'initialisation de la base de données
init_db()


@app.route('/')
def home():
    global count
    count = incrementer_compteur()
    return render_template('home.html',count=count)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form')
def form():
    return render_template('form.html')

#app.run()                            # démarrage de l’application
app.run(host="0.0.0.0")               # pour que ma machine soit visible pour tout le monde                       
