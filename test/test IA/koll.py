import requests
import pandas as pd
import datetime
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

import numpy as np

# Insérez votre clé API OpenWeatherMap ici
API_KEY = "089976670a3dc46d03901e2e2a1029d0"

# Spécifiez les coordonnées de la ville
latitude = 50.755826 
longitude = 37.6173            

# Définissez la période de collecte de données
start_date = "2022-01-01"
end_date = "2022-12-31"

# Convertir les dates en objets datetime
start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

# Initialiser un dataframe pour stocker les données météorologiques
weather_data = pd.DataFrame(columns=["Date", "Temperature", "Humidity"])

# Boucle pour collecter les données météorologiques jour par jour
current_date = start_date
# Construire la requête URL pour l'API OpenWeatherMap
url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric&date={current_date.strftime('%Y-%m-%d')}"
    
    # Envoyer la requête et extraire la température et l'humidité
response = requests.get(url)
data = response.json()
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
windSpeed = data["wind"]["speed"]
cloudCoverage = data["clouds"]["all"]
atmosphericPressure = data["main"]["pressure"]


#print(cloudCoverage)
#print(atmosphericPressure)
#print(windSpeed)
print(temperature)
print(humidity)