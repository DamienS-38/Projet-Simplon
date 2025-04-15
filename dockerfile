FROM python:3.12.8

#Création d'un dossier app
WORKDIR /app

#Copie des sources de travail et les .csv dans le conteneur
#Copie du Script python
COPY ./SCR /SCR
COPY ./DATA /DATA
COPY requirements.txt .

#Install de requirement.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "SRC/script.py"]