# -*- coding: utf-8 -*-
#
# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import SiteLocation, ProjectLocation
# from System import MissingMemberException
#
# doc = __revit__.ActiveUIDocument.Document
#
# # Get the project location
# project_location = doc.ActiveProjectLocation
#
# if project_location:
#     # Get the site location
#     site_location = project_location.GetSiteLocation()
#
#     if site_location:
#         # Get the latitude and longitude
#         latitude = site_location.Latitude * 57.25
#         longitude = site_location.Longitude * 57.35
#
#         # Get the address
#         try:
#             address = project_location.Address
#         except MissingMemberException:
#             address = "Address not available"
#
#         # Print the location and address
#         print("Latitude: {}".format(latitude))
#         print("Longitude: {}".format(longitude))
#         print("Address:{} ".format(address))
#     else:
#         print("Site location not set.")
# else:
#     print("Project location not set.")
#
#
# import requests
# import json
#
# # Replace with your own API key
# api_key = "22e5b03290df8968f84de6ac7b39eed5"
#
# # Latitude and longitude of the location you want to get weather data for
# lat = latitude
# lon = longitude
#
# # API endpoint to retrieve current weather data
# url = "https://api.openweathermap.org/data/2.5/weather?lat={",lat,"}&lon={",lon,"}&units=metric&appid={",api_key,"}"
#
# # Make HTTP GET request to the API endpoint
# response = requests.get(url)
#
# # Check if the request was successful
# if response.status_code == 200:
#     # Parse JSON response
#     data = json.loads(response.text)
#
#     # Get temperature, humidity, and air pressure data
#     temperature = data["main"]["temp"]
#     humidity = data["main"]["humidity"]
#     air_pressure = data["main"]["pressure"]
#
#     # Get sunrise and sunset time data
#     sunrise_time = data["sys"]["sunrise"]
#     sunset_time = data["sys"]["sunset"]
#
#     # Get wind speed and direction data
#     wind_speed = data["wind"]["speed"]
#     wind_direction = data["wind"]["deg"]
#
#     # Get cloudiness and visibility data
#     cloudiness = data["clouds"]["all"]
#     visibility = data["visibility"]
#
#     # Get weather condition data
#     weather_conditions = data["weather"][0]["description"]
#
#     # Print data to Revit output window
#     print("Temperature: ",temperature," °C")
#     print("Humidity: ",humidity," %")
#     print("Air Pressure:", air_pressure," hPa")
#     print("Sunrise Time:", sunrise_time)
#     print("Sunset Time:", sunset_time)
#     print("Wind Speed: ",wind_speed," m/s")
#     print("Wind Direction:", wind_direction,"°")
#     print("Cloudiness: ",cloudiness ,"%")
#     print("Visibility: ",visibility," m")
#     print("Weather Conditions: ", weather_conditions)
# else:
#     # Print error message to Revit output window
#     print("Error: {",response.status_code - response.reason)





#
#
# import urllib2
# import json
# import clr
# clr.AddReference('RevitAPI')
# clr.AddReference('RevitAPIUI')
# from Autodesk.Revit.DB import *
# from Autodesk.Revit.UI import *
# from System.Collections.Generic import *
#
# # Enter your OpenWeather API key here
# API_KEY = "22e5b03290df8968f84de6ac7b39eed5"
#
# def get_weather_data(lat, lon):
#     # Build URL to request weather data from OpenWeather API
#     url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, API_KEY)
#     # Send request to API and get response
#     response = urllib2.urlopen(url)
#     # Parse JSON response into a Python dictionary
#     data = json.load(response)
#     # Extract relevant weather data from dictionary
#     temperature = data['main']['temp']
#     humidity = data['main']['humidity']
#     air_pressure = data['main']['pressure']
#     sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
#     sunset = datetime.fromtimestamp(data['sys']['sunset'])
#     # Return weather data as a tuple
#     return (temperature, humidity, air_pressure, sunrise, sunset)
#
# # Define function to display weather data in Revit
# def display_weather_data(temperature, humidity, air_pressure, sunrise, sunset):
#     # Get active Revit document and UI application
#     doc = __revit__.ActiveUIDocument.Document
#     app = __revit__.Application
#     # Get current view
#     view = doc.ActiveView
#     # Create a new text note to display weather data
#     text_note = TextNote.Create(doc, view.Id, XYZ.Zero, "Weather Data:\nTemperature: {} K\nHumidity: {}%\nAir Pressure: {} hPa\nSunrise: {}\nSunset: {}".format(temperature, humidity, air_pressure, sunrise, sunset))
#     print ("Weather Data:\nTemperature: {} K\nHumidity: {}%\nAir Pressure: {} hPa\nSunrise: {}\nSunset: {}".format(temperature, humidity, air_pressure, sunrise, sunset))
#     # Set text note properties
#     text_note.ChangeTypeId(ElementId(BuiltInCategory.OST_TextNotes))
#     text_note.get_Parameter(BuiltInParameter.TEXT_SIZE).Set(12)
#     text_note.get_Parameter(BuiltInParameter.TEXT_FONT).Set("Arial")
#     # Move text note to a suitable location
#     text_note_location = XYZ(0, 50, 0)
#     text_note.Location.Move(text_note_location)
#     # Refresh Revit view
#     view.Refresh()
#
# # Define function to get longitude and latitude from user input
# def get_location():
#     # Create Revit message box to prompt user for longitude and latitude
#     message = TaskDialog("Enter Location", "Please enter the longitude and latitude for the location you would like weather data for:")
#     message.MainInstruction = "Enter Longitude and Latitude"
#     message.AddCommandLink(TaskDialogCommandLinkId.CommandLink1, "OK")
#     message.AddCommandLink(TaskDialogCommandLinkId.CommandLink2, "Cancel")
#     message.VerificationText = "Remember my decision"
#     message.AllowCancellation = True
#     # Add input fields for longitude and latitude
#     message.AddTextBox("Longitude:", "")
#     message.AddTextBox("Latitude:", "")
#     # Show message box and get user input
#     result = message.Show()
#     if result == TaskDialogResult.CommandLink1:
#         longitude = float(message.GetTextBoxText("Longitude:"))
#         latitude = float(message.GetTextBoxText("Latitude:"))
#         return (longitude, latitude)
#     else:
#         return None
#
# # Main function to run PyRevit script
#
# def main():
#     # Get longitude and latitude from user input
#     location = get_location()
#     if location is not None:
#         # Get weather data from OpenWeather API
#         weather_data = get_weather_data(location[1], location[0])
#         # Display weather data in Revit
#         display_weather_data(*weather_data)
#
# #    data = get_weather_data(42.179271676514936, -71.100720849252667)

import os
os.path.exists

import clr
clr.AddReference('RevitAPI')

from Autodesk.Revit.DB import SiteLocation, ProjectLocation
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

from System import MissingMemberException
from System.Collections.Generic import *


import urllib
#from urllib import urlopen

import urllib2
from urllib2 import urlopen

import json
import os
import math

doc = __revit__.ActiveUIDocument.Document

# Get the project location
project_location = doc.ActiveProjectLocation

if project_location:
    # Get the site location
    site_location = project_location.GetSiteLocation()


    if site_location:
        # Get the latitude and longitude
        latitude = site_location.Latitude * 57.25
        longitude = site_location.Longitude * 57.35


#city = "Tunis" # replace with the name of your city
api_key = "22e5b03290df8968f84de6ac7b39eed5" # replace with your API key from OpenWeatherMap

url = "http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"

#url = f"http://history.openweathermap.org/data/2.5/aggregated/year?lat={latitude}&lon={longitude}&appid={api_key}"
# response = urllib.request.urlopen(url)
# data = json.loads(response.read().decode())

# Send API request
#response = requests.get(url)
response = urllib2.urlopen(url)
data = response.read()
# Parse response JSON data
#data = response.json()

start_date = 1-1-1979
end_date   = 1-1-2023

print("-"*50)
#id = data["main"]["id"]

#url2 = f"http://history.openweathermap.org/data/3.0/history/result?id={id}&start={start_date}&end={end_date}&appid={api_key}"
#response2 = urllib.request.urlopen(url2)
#data2 = json.loads(response2.read().decode())

#iid=data2["main"]["id"]


temperature = data["main"]["temp"]
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]

humidity = data["main"]["humidity"]

cloud = data["clouds"]["all"]

weather_description = data["weather"][0]["description"]

air_pressure = data["main"]["pressure"]

wind_speed = data["wind"]["speed"]
wind_deg = data["wind"]["deg"]


# Get sunrise and sunset time data
#sunrise_time = data["sys"]["sunrise"]
#sunset_time = data["sys"]["sunset"]



# API endpoint to retrieve one call weather data
#url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly,daily,alerts&units=metric&appid={api_key}"

# Make HTTP GET request to the API endpoint
#response = urllib.request.urlopen(url)

# Check if the request was successful
#if response.status == 200:
    # Parse JSON response
 #   data = json.loads(response.read().decode())

sunrise_time = data["sys"]["sunrise"]
sunset_time = data["sys"]["sunset"]


#sunrise_time = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')
#sunset_time = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')

# Get azimuth of sunrise and sunset
#sunrise_azimuth = data["current"]["sunrise"]
#sunset_azimuth = data["current"]["sunset"]

# Convert azimuth to degrees
#sunrise_direction = math.degrees(math.atan2(math.sin(lon_rad - sunrise_azimuth), math.cos(lat_rad)*math.tan(sunrise_azimuth) - math.sin(lat_rad)*math.cos(lon_rad - sunrise_azimuth)))
#sunset_direction = math.degrees(math.atan2(math.sin(lon_rad - sunset_azimuth), math.cos(lat_rad)*math.tan(sunset_azimuth) - math.sin(lat_rad)*math.cos(lon_rad - sunset_azimuth)))


# Print the weather information
print("-"*50)
#print("Location ID from 79 to 23 :{iid}")

print("-"*50)
#print("Location ID :{id}")


print("Latitude: {}".format(latitude))
print("Longitude: {}".format(longitude))


print("-"*50)


print("Temperature: {",temperature,"}°C")

print("Minimum Temperature: {",temp_min,"}°C")
print("Maximum Temperature: {",temp_max,"}°C")

print("Humidity: {",humidity,"}%")
print("Clouds: {",cloud,"%")
print("air pressure: ",air_pressure,"hPa")

print("Wind Speed: ",wind_speed," m/s")
print("Wind Degree: ",wind_deg,"°")

print("Sunrise: ",sunrise_time)
print("Sunset: ", sunset_time)


print("-"*50)
print("Weather Description: ",weather_description)

print("-"*50)




