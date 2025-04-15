FROM python:3.12.8

# Labels pour les métadonnées
LABEL maintainer="Schaeffer <damien.schaeffer@gmail.com>"
LABEL version="1.0"
LABEL description="Projet Simplon"

#Création d'un dossier app
WORKDIR /app

# Ajout de sqlite3 CLI
RUN apt update && apt install -y sqlite3

#Copie des sources de travail et les .csv dans le conteneur
#Copie du Script python
COPY ./SRC /SRC
COPY ./DATA /DATA
COPY requirements.txt .

#Install de requirement.txt
RUN pip install --no-cache-dir -r requirements.txt

#CMD ["python", "hello.py"]
CMD ["python", "SRC/script.py"]
