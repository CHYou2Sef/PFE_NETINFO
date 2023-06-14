# # -*- coding: utf-8 -*-

__name__ = "Yearly Weather"
__title__ = "Weather"
__doc__   = "Version 1.0"

import urllib
from urllib2 import *

from urllib import urlopen

import json
import math

import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import SiteLocation, ProjectLocation
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

from System import MissingMemberException
from System.Collections.Generic import *

doc = __revit__.ActiveUIDocument.Document

# Get the project location
project_location = doc.ActiveProjectLocation

if project_location:
    # Get the site location
    site_location = project_location.GetSiteLocation()

    if site_location:
        # Get the latitude and longitude
        latitude = site_location.Latitude * 57.295779513082371657204904505678
        longitude = site_location.Longitude * 57.295779513082106043773967605463

print(latitude)
print(longitude)
api_key = "22e5b03290df8968f84de6ac7b39eed5"  # replace with your API key from OpenWeatherMap

# API = "73b3f6dc84c843379eb174344230304"  # My Weather API
# ex id : 2468579

url2 = "http://api.openweathermap.org/data/2.5/weather?lat={",latitude,"}&lon={",longitude,"}&appid={",api_key,"}&units=Metric"

response = urllib.urlopen(url2)
data2 = response.read()



id = data2["id"]
name = data2["name"]

print (id ,"/", name)

url = "https://history.openweathermap.org/data/2.5/aggregated/year?id={",id,"}&appid={",api_key,"}"

# url = fhttps://history.openweathermap.org/data/2.5/history/city?lat={latitude}&lon={longitude}&appid={api_key}"
# url = fhttp://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=Metric"

#this is the true and correct in the revit python shell
response = urllib.urlopen(url)
data = response.read()
#response = urllib.request.urlopen(url)
#data = json.loads(response.read().decode())

print("+" * 100)
# print(data)
city_id = data["city_id"]
print("The city name {",name,"} is and ID is {",city_id,"}.")

i = 0
lenght = data["result"]
# print(type(lenght))
# print(len(lenght))
temp_data = []
hum_data = []
wind_data = []
per_data = []
cloud_data = []

for i in range(len(data["result"])):
    temp_data.append(data["result"][i]["temp"]["median"] - 273.15)

for i in range(len(data["result"])):
    hum_data.append(data["result"][i]["humidity"]["median"])

for i in range(len(data["result"])):
    wind_data.append(data["result"][i]["wind"]["median"])

for i in range(len(data["result"])):
    per_data.append(data["result"][i]["precipitation"]["mean"])

for i in range(len(data["result"])):
    cloud_data.append(data["result"][i]["clouds"]["mean"])

# print (type(year_data))
# print (year_data)
# Calculate the average temperature for the year

avg_temp = sum(temp_data) / len(temp_data)
avg_humi = sum(hum_data) / len(hum_data)
avg_wind = sum(wind_data) / len(wind_data)
avg_cloud = sum(cloud_data) / len(cloud_data)
avg_perc = sum(per_data) / len(per_data)

print("The average weather parameters values in {} for this year was : ".format(name))
print("The average temperature : 	 {:.1f} °C".format(avg_temp))
print("The average humidity :  	 {:.2f} % ".format(avg_humi))
print("The average wind : 			 {:.2f} metre/sec".format(avg_wind))
print("The average precipitation :  {:.2f} mm/h".format(avg_perc))
print("The average cloud : 		 {:.2f} %".format(avg_cloud))

# temps = [day_data["temp"]["avg"] for month_data in year_data for day_data in month_data.values()]
# avg_temp = sum(temps) / len(temps)
# print(f"The average temperature in Los Angeles for 2022 was {avg_temp:.2f} degrees Celsius.")

# year_data = data["result"]["2022"]
# temps = [day_data["temp"]["avg"] for month_data in year_data.values() for day_data in month_data.values()]
# avg_temp = sum(temps) / len(temps)
# print(f"The average temperature in Los Angeles for 2022 was {avg_temp:.1f} degrees Celsius.")

print("+" * 100)

with open("Y:\\0000\Etud\pythonRevit\FirstBtn.extension\lib\DB\Parameters.txt", "w") as f:
    # with open("C:\\Users\YOUSSEF\PFE\Parameters.txt", "w") as f:
    f.write(
        "{}\n{}\n{:.2f}\n{:.2f}\n{:.2f}\n{:.2f}\n{:.2f}\n{:.2f}\n{:.2f}\n".format(city_id, name, latitude, longitude,
                                                                                  avg_temp, avg_humi, avg_wind,
                                                                                  avg_cloud, avg_perc))
f.close()

with open("Y:\\0000\Etud\pythonRevit\FirstBtn.extension\lib\DB\TotalPower.txt", "w") as f:
    # with open("C:\\Users\YOUSSEF\PFE\Temp.txt", "w") as f:
    f.write("{:.2f}".format(avg_temp))
f.close()


