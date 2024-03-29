import requests
import pandas as pd
import datetime
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
import math
import numpy as np

# Insérez votre clé API OpenWeatherMap ici
API_KEY = "089976670a3dc46d03901e2e2a1029d0"

# Spécifiez les coordonnées de la ville
latitude = 55.755826 
longitude = 37.6173            

# Définissez la période de collecte de données
start_date = "2022-01-01"
end_date = "2022-12-31"

# Convertir les dates en objets datetime
start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

# Initialiser un dataframe pour stocker les données météorologiques
weather_data = pd.DataFrame(columns=["Date", "Temperature", "Humidity","speed","pressure"])

# Boucle pour collecter les données météorologiques jour par jour
current_date = start_date
while current_date <= end_date:
    # Construire la requête URL pour l'API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric&date={current_date.strftime('%Y-%m-%d')}"
    
    # Envoyer la requête et extraire la température et l'humidité
    response = requests.get(url)
    data = response.json()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    windSpeed = data["wind"]["speed"]
    atmosphericPressure = data["main"]["pressure"]
    
    
    # Ajouter les données à la dataframe
    weather_data = pd.concat([weather_data, pd.DataFrame([[current_date, temperature, humidity, windSpeed,atmosphericPressure]], columns=["Date", "Temperature", "Humidity","speed","pressure"])], ignore_index=True)

    # Incrémenter la date courante
    current_date += datetime.timedelta(days=1)
weather_data.to_csv("weather_data.csv", index=False)

# Calculez la température et l'humidité moyennes pour toute l'année
mean_temperature = weather_data['Temperature'].mean()
mean_humidity = weather_data['Humidity'].mean()
mean_speed = weather_data['speed'].mean()
mean_pressure = weather_data['pressure'].mean()




temp = math.ceil(mean_temperature)
hum=math.ceil(mean_humidity)
speed=math.ceil(mean_speed)
pressure=math.ceil(mean_pressure)

# Afficher les températures et humidités moyennes pour l'année
print(f"La température moyenne pour l'année 2022 est de {temp}°C")
print(f"L'humidité moyenne pour l'année 2022 est de {hum}%")
print(f"La vitese de vent moyenne pour l'année 2022 est de {speed}m/s")
print(f"La valeur de mouenne de pression pour l'année 2022 est de {pressure}hPa")


data= pd.read_csv("data.csv")
print(data)

X = data[['tempirature', 'humidite', 'vitesse de vent','pression']]
y1 = data[['materiau_fenetre']]
y2 = data[['materiau_porte']]
y3 = data[['materiau_mur']]

y1 = np.ravel(y1.values)
y2 = np.ravel(y2.values)
y3 = np.ravel(y3.values)

X_train, X_test, y1_train, y1_test = train_test_split(X, y1, test_size=0.2, random_state=0)
_, _, y2_train, y2_test = train_test_split(X, y2, test_size=0.2, random_state=0)
_, _, y3_train, y3_test = train_test_split(X, y3, test_size=0.2, random_state=0)

model1 = DecisionTreeClassifier()
model1.fit(X_train, y1_train)

model2 = DecisionTreeClassifier()
model2.fit(X_train, y2_train)

model3 = DecisionTreeClassifier()
model3.fit(X_train, y3_train)

Txerreur=(1-model1.score(X_test,y2_test))
print("Taux d'erreur sur l'ensemble de test:", Txerreur)

accuracy1 = model1.score(X_test, y1_test)
print('Précision matériau fenêtre: ', accuracy1)

accuracy2 = model2.score(X_test, y2_test)
print('Précision matériau porte: ', accuracy2)

accuracy3 = model3.score(X_test, y3_test)
print('Précision matériau mur: ', accuracy3)

input = [[temp,hum,speed,pressure]]

output1 = model1.predict(input)
print('Matériau fenêtre: ', output1)

output2 = model2.predict(input)
print('Matériau porte: ', output2)

output3 = model3.predict(input)
print('Matériau mur: ', output3)