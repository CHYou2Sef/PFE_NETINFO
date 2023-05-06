# Import necessary modules
import clr
import sys
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import statistics
import inspect

# Add Revit API and PyRevit to system path
sys.path.append(r'Y:\Autodesk\Revit 2021\RevitAPI.dll')
sys.path.append(r'C:\Users\YOUSSEF\AppData\Roaming\pyRevit-Master\pyrevitlib')

# Import Revit API modules
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

# Get the project location
project_location = doc.ActiveProjectLocation

if project_location:
    # Get the site location
    site_location = project_location.GetSiteLocation()

    if site_location:
        # Get the latitude and longitude
        latitude = site_location.Latitude * 57.249999999999998485725513764567
        longitude = site_location.Longitude * 57.349999999999999822928494065878


# # Set up Firebase Realtime Database
# cred = credentials.Certificate('path/to/serviceAccountKey.json')
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://your-firebase-project.firebaseio.com/'
# })

# Set up API request parameters
# API_KEY = 'your_api_key_here'
# CITY_ID = 'city_id_here'

START_YEAR = 2000
END_YEAR = 2020

# Retrieve the medium temperature data
temps = []
for year in range(START_YEAR, END_YEAR):
    response = requests.get('http://api.openweathermap.org/data/3.0/onecall/timemachine?lat={',latitude,'}&lon={',longitude,'}&dt={',year-01-01,'}&appid=7741a241ee574c0ab1b133333231804&units=metric')
    data = response.json()
    temp = data['current']['temp']
    temps.append(temp)
medium_temp = statistics.median(temps)

# Save temperature data to Firebase Realtime Database
ref = db.reference('temperature')
ref.set({
    'medium_temp': medium_temp
})

# Show a message box with the medium temperature data
TaskDialog.Show('Medium Temperature', 'The medium temperature of the last 10 years is {',medium_temp,'} degrees Celsius.')
