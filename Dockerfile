FROM python:3.10


RUN pip install poetry      # pour installer poetry dans le container

WORKDIR /app   # app : un nom qu'on a donné au dossier qui est dans le container
COPY . /app/.  # copier ce qui est dans le dossier machine, et le mettre dans le dossier app qui est dans le container

RUN poetry config virtualenvs.create false  # cad désactiver l'environnement virtuel qu'on a crée avec pyenv
					    # pour ne pas le copier dans le container, car le container est déja un evironnement virtuel (isolé)
					     
RUN poetry install                          #   pour installer les dépendances crées avec poetry sur notre machine   

EXPOSE 5000				 # le port du container
ENTRYPOINT ["python"]			  # ENTRYPOINT permet de configurer un container qui va alors fonctionner comme un exécutable.
CMD ["my_app.py"]                        # The CMD instruction sets the command to be executed when running a container from an image.
					 # => 
