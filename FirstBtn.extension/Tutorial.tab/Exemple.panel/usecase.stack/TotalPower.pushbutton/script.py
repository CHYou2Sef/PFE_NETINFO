# -*- coding: utf-8 -*-

__title__ = ' Thermal balance  '
__author__ = 'Chebl Youssef'

"""Show all Thermal balance  infomation of the project..."""

import os
os.path.exists

import urllib
from urllib import urlopen

# import pyrevit
import math
# __context__ = 'Selection'

# Import the necessary modules
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *

#from pyrevit import requests

from pyrevit import revit, DB
import os
os.path.exists
# Get the active Revit document
doc = __revit__.ActiveUIDocument.Document

# Create a FilteredElementCollector to get all the windows
windows = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType().ToElements()
walls   = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()
roofs   = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Roofs).WhereElementIsNotElementType().ToElements()
floors  = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType().ToElements()
doors   = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElements()


numRoof  = 0
numFloor = 0
numWind  = 0
numWall  = 0
numDoor  = 0

TPDoor  = 0
TPFloor = 0
TPRoof  = 0
TPWind  = 0
TPWall  = 0

f = open("C:\\Users\\YOUSSEF\\PFE\\Temp.txt", "r")
Tex = float(f.read())
f.close()


print("*" * 100)
#Bilan thermique
print ("***         Thermal balance      ***")

# Loop through the windows and do something with them
print("*"*100)
print("Windows family :")
print("*"*100)
for window in windows:
    numWind += 1
    id         = window.Id
    element    = doc.GetElement(id)
    name       = window.Name
    print ("*"*10)
    print ("ID = {}".format(id.IntegerValue) )
    print ("Name : {}".format(name) )
    # print("UniqueId :",window.UniqueId)
    # # print("Location :",window.Location.ToString)
    # print("IsValidObject :",window.IsValidObject)
    # print("IsTransient :",window.IsTransient )
    # print("Category :",window.Category)

    cons   = element.Symbol.GetThermalProperties().AnalyticConstructionName
    u_val  = element.Symbol.GetThermalProperties().HeatTransferCoefficient
    r_val  = element.Symbol.GetThermalProperties().ThermalResistance
    vis    = element.Symbol.GetThermalProperties().VisualLightTransmittance

    # print ("It has Thermal Properties ?")
    # print(element.Symbol.HasThermalProperties())
    # print ("The construction gbXML name:",cons)
    # print ("The transfer  coefficient value (U-Value):",u_val)
    # print ("The thermal resistance value (R-Value): ",r_val)
    # print ("The visual light transmittance: ",vis)

    surf = 0
    param_set = window.Parameters
    # PRINT PARAMETER VALUES FOR THE SELECTED ELEMENT
    print("Parameter Values:")
    for param in param_set:
        #print(param.Definition.Name, param.AsString(), param.AsValueString(), param.AsDouble())
        #print("Storage type: ", param.StorageType, ", read only :", param.IsReadOnly)
        if (param.Definition.Name == "Surface"):
            surf = param.AsDouble()
    s = math.ceil(surf) / 10


    #Calcul la puissance de chauffage (déperdition surfacique)
    print ("***Calculation of heating power (area loss) \n θ (W) = H * ∆T")
    print ("Surface = {} m²".format(s))
    print ("U = {} W/(m²/K)".format(u_val))

    H = u_val * s
    print ("{} * {} = {} W/m².K".format(u_val, s, H))
    #le coefficient de déperdition
    print ("= {} W/m².K ".format(H))

    # En fixe à 20 °C la température résultante que les équipements de chauffage doivent permettre de maintenir au centre des pièces des logements
    print ("By fixing the indoor temperature at 20°C and outdoor at {}°C".format(Tex))
    Pch = H * (20 - Tex)
    print ("{} * (20 - {}) = {} W ".format(H, Tex, Pch))
    #la puissance de chauffage
    print ("the heating power of {} = {} W ".format(name,Pch))
    TPWind += Pch
    print ("-" * 10)
    #La totale de puissance de chauffage des  fenetres
print ("The total heating power of the  {} windows = {}W".format(numWind ,TPWind))


# Loop through the doors and do something with them
print("*"*100)
print("Doors family :")
print("*"*100)
for door in doors:
    numDoor += 1
    id         = door.Id
    element    = doc.GetElement(id)
    name       = door.Name
    print ("*"*10)
    print ("ID = {}".format(id.IntegerValue) )
    print ("Name : {}".format(name) )
    # print("UniqueId :",window.UniqueId)
    # # print("Location :",window.Location.ToString)
    # print("IsValidObject :",window.IsValidObject)
    # print("IsTransient :",window.IsTransient )
    # print("Category :",window.Category)

    #cons   = element.Symbol.GetThermalProperties().AnalyticConstructionName
    u_val  = element.Symbol.GetThermalProperties().HeatTransferCoefficient
    #r_val  = element.Symbol.GetThermalProperties().ThermalResistance
    #vis    = element.Symbol.GetThermalProperties().VisualLightTransmittance
    if (u_val == None):
        forms.alert
    # print ("It has Thermal Properties ?")
    # print(element.Symbol.HasThermalProperties())
    # print ("The construction gbXML name:",cons)
    # print ("The transfer  coefficient value (U-Value):",u_val)
    # print ("The thermal resistance value (R-Value): ",r_val)
    # print ("The visual light transmittance: ",vis)

    surf = 0
    param_set = door.Parameters
    # PRINT PARAMETER VALUES FOR THE SELECTED ELEMENT
    print("Parameter Values:")
    for param in param_set:
        #print(param.Definition.Name, param.AsString(), param.AsValueString(), param.AsDouble())
        #print("Storage type: ", param.StorageType, ", read only :", param.IsReadOnly)
        if (param.Definition.Name == "Surface"):
            surf = param.AsDouble()
    s = math.ceil(surf) / 10


    #Calcul la puissance de chauffage (déperdition surfacique)
    print ("***Calculation of heating power (area loss) \n θ (W) = H * ∆T")
    print ("Surface = {} m²".format(s))
    print ("U = {} W/(m²/K)".format(u_val))

    H = u_val * s
    print ("{} * {} = {} W/m².K".format(u_val, s, H))
    #le coefficient de déperdition
    print ("H = {} W/m².K ".format(H))

    # En fixe à 20 °C la température résultante que les équipements de chauffage doivent permettre de maintenir au centre des pièces des logements
    print ("By fixing the indoor temperature at 20°C and outdoor at {}°C".format(Tex))
    Pch = H * (20 - Tex)
    print ("{} * (20 - {}) = {} W ".format(H, Tex, Pch))
    #la puissance de chauffage
    print ("the heating power of {} = {} W ".format(name,Pch))
    TPDoor += Pch
    print ("-" * 10)
    #La totale de puissance de chauffage des  fenetres
print ("The total heating power of the  {} doors = {}W".format(numDoor ,TPDoor))

print("*"*100)
print("Walls family :")
print("*"*100)
# Loop through the walls and do something with them
for wall in walls:
    numWall += 1
    id         = wall.Id
    element    = doc.GetElement(id)
    name       = wall.Name
    print("*"*10)
    print ("ID",id.IntegerValue )
    print("Name :",name)
    if element.WallType.ThermalProperties == None :
        print ("This Wall has not Thermal Properties ..")
        break
    else:
        Abso   = element.WallType.ThermalProperties.Absorptance
        u_val  = element.WallType.ThermalProperties.HeatTransferCoefficient
        r_val  = element.WallType.ThermalProperties.ThermalResistance
        Roug    = element.WallType.ThermalProperties.Roughness

        # print ("It has Thermal Properties ?")
        # print(element.WallType.HasThermalProperties())
        # print ("The construction gbXML name:",Abso)
        # print ("The transfer  coefficient value (U-Value):",u_val)
        # print ("The thermal resistance value (R-Value): ",r_val)
        # print ("The visual light transmittance: ",Roug)

        surf = 0
        param_set = wall.Parameters
        # PRINT PARAMETER VALUES FOR THE SELECTED ELEMENT
        print("Parameter Values :")
        for param in param_set:
            # print(param.Definition.Name, param.AsString(), param.AsValueString(), param.AsDouble())
            # print("Storage type: ", param.StorageType, ", read only :", param.IsReadOnly)
            if (param.Definition.Name == "Surface"):
                surf = param.AsValueString()
        # s = math.ceil(surf) / 10

        x = surf.split()
        num1 = x[0]
        #print(num1)
        #print(type(num1))
        num2 = float(num1)
        #print(num2)
        #print(type(num2))

        # Calcul la puissance de chauffage (déperdition surfacique)
        print ("*** Calculation of heating power (area loss) \n θ(W) = H * ∆T")
        print ("Surface = {} m²".format(num2))
        print ("U = {} W/(m²/K)".format(u_val))
        H = u_val * num2
        print ("{} * {} = {} W/m².K".format(u_val, num2, H))
        # le coefficient de déperdition
        print ("the wastage coefficient = {} W/m².K ".format(H))


        # En fixe à 20 °C la température résultante que les équipements de chauffage doivent permettre de maintenir au centre des pièces des logements
        print ("By fixing the indoor temperature at 20°C and outdoor at {}°C".format(Tex))
        Pch = H * (20 - Tex)
        print ("{} * (20 - {}) = {} W ".format(H, Tex, Pch))
        #la puissance de chauffage
        print ("the heating power of '{}' = {} W ".format(name,Pch))
        TPWall += Pch
        print ("-" * 10)
#La totale de puissance de chauffage des murs
print ("The total heating power of the  {} walls = {} W".format(numWall, TPWall))



print("*"*100)
print("Roofs family :")
print("*"*100)
# Loop through the roofs and do something with them
for floor in roofs:
    numRoof += 1
    id         = floor.Id
    element    = doc.GetElement(id)
    name       = floor.Name
    print("*"*10)
    print ("ID",id.IntegerValue )
    print("Name :",name)
    Abso   = element.RoofType.ThermalProperties.Absorptance
    u_val  = element.RoofType.ThermalProperties.HeatTransferCoefficient
    r_val  = element.RoofType.ThermalProperties.ThermalResistance
    Roug    = element.RoofType.ThermalProperties.Roughness

    # print ("It has Thermal Properties ?")
    # print(element.WallType.HasThermalProperties())
    # print ("The construction gbXML name:",Abso)
    # print ("The transfer  coefficient value (U-Value):",u_val)
    # print ("The thermal resistance value (R-Value): ",r_val)
    # print ("The visual light transmittance: ",Roug)

    surf = 0
    param_set = floor.Parameters
    # PRINT PARAMETER VALUES FOR THE SELECTED ELEMENT
    print("Parameter Values:")
    for param in param_set:
        # print(param.Definition.Name, param.AsString(), param.AsValueString(), param.AsDouble())
        # print("Storage type: ", param.StorageType, ", read only :", param.IsReadOnly)
        if (param.Definition.Name == "Surface"):
            surf = param.AsValueString()
    #s = math.ceil(surf) / 10
    #s = surf

    x = surf.split()
    num1 = x[0]
    # print(num1)
    # print(type(num1))
    num2 = float(num1)
    # print(num2)
    # print(type(num2))

    # Calcul la puissance de chauffage (déperdition surfacique)
    print ("*** Calculation of heating power (area loss)  \n θ(W) = H * ∆T")
    print ("Surface = {} m²".format(num2))
    print ("U = {} W/(m²/K)".format(u_val))
    H = u_val * num2
    print ("{} * {} = {} W/m².K".format(u_val, num2, H))
    # le coefficient de déperdition
    print ("the wastage coefficient = {} W/m².K ".format(H))


    # En fixe à 20 °C la température résultante que les équipements de chauffage doivent permettre de maintenir au centre des pièces des logements
    print ("By fixing the indoor temperature at 20°C and outdoor at {}°C".format(Tex))
    Pch = H * (20 - Tex)
    print ("{} * (20 - {}) = {} W ".format(H, Tex, Pch))
    #la puissance de chauffage
    print ("the heating power of '{}' = {}W ".format(name,Pch))
    TPRoof += Pch
    print ("-" * 10)
#La totale de puissance de chauffage des toit
print ("The total heating power of the {} roofs = {}W".format(numRoof, TPRoof))



print("*"*100)
print("Floors family :")
print("*"*100)
# Loop through the roofs and do something with them
for floor in floors:
    numFloor += 1
    id         = floor.Id
    element    = doc.GetElement(id)
    name       = floor.Name
    print("*"*10)
    print ("ID",id.IntegerValue )
    print("Name :",name)
    Abso   = element.FloorType.ThermalProperties.Absorptance
    u_val  = element.FloorType.ThermalProperties.HeatTransferCoefficient
    r_val  = element.FloorType.ThermalProperties.ThermalResistance
    Roug    = element.FloorType.ThermalProperties.Roughness

    # print ("It has Thermal Properties ?")
    # print(element.WallType.HasThermalProperties())
    # print ("The construction gbXML name:",Abso)
    # print ("The transfer  coefficient value (U-Value):",u_val)
    # print ("The thermal resistance value (R-Value): ",r_val)
    # print ("The visual light transmittance: ",Roug)

    surf = 0
    param_set = floor.Parameters
    # PRINT PARAMETER VALUES FOR THE SELECTED ELEMENT
    print("Parameter Values :")
    for param in param_set:
        #print(param.Definition.Name, param.AsString(), param.AsValueString(), param.AsDouble())
        #print("Storage type: ", param.StorageType, ", read only :", param.IsReadOnly)
        if (param.Definition.Name == "Surface"):
            surf = param.AsValueString()
    #s = math.ceil(surf) / 10
    #s = surf

    x = surf.split()
    num1 = x[0]
    # print(num1)
    # print(type(num1))
    num2 = float(num1)
    # print(num2)
    # print(type(num2))

    #Calcul la puissance de chauffage (déperdition surfacique)
    print ("*** Calculation of heating power (area loss)  \n θ(W) = H * ∆T")

    print ("Surface = {} m²".format(num2))
    print ("U = {} W/(m²/K)".format(u_val))
    H = u_val * num2
    print ("{} * {} = {} W/m².K".format(u_val, num2, H))
    # le coefficient de déperdition
    print ("the wastage coefficient = {} W/m².K ".format(H))


    # En fixe à 20 °C la température résultante que les équipements de chauffage doivent permettre de maintenir au centre des pièces des logements
    print ("By fixing the indoor temperature at 20°C and outdoor at {}°C ".format(Tex))
    Pch = H * (20 - Tex)
    print ("{} * (20 - {}) = {} W ".format(H, Tex, Pch))
    #la puissance de chauffage
    print ("the heating power of '{}' = {} W ".format(name,Pch))
    TPFloor += Pch
    print ("-" * 10)
#La totale de puissance de chauffage des toit
print ("The total heating power of the {} floors = {}W".format(numFloor, TPFloor))

TT = TPFloor + TPWall + TPWind + TPRoof

print("*"*100)
print ("The total heating power of the project = {}W".format(TT))
print("*"*100)


with open("C:\Users\YOUSSEF\PFE\TotalPower.txt", "w") as f:
    f.write("{}".format(TT))

f.close()

