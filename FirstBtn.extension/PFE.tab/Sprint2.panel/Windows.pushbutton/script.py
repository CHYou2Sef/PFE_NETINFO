# -*- coding: utf-8 -*-

__title__ = 'All Windows Data '
__author__ = 'Chebl Youssef'

from Autodesk.Revit.DB import BuiltInCategory
from Autodesk.Revit.DB import FilteredElementCollector

"""Show all windows infomation..."""

import os
os.path.exists

# import pyrevit
import math
# __context__ = 'Selection'

# Import the necessary modules
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *

from pyrevit import revit, DB
import os
os.path.exists
# Get the active Revit document
doc = __revit__.ActiveUIDocument.Document

#f = open("C:\\Users\\YOUSSEF\\PFE\\Temp.txt", "r")
f = open("Y:\\0000\\Etud\\pythonRevit\\FirstBtn.extension\\lib\\DB\\Temp.txt", "r")

Tex = float(f.read())
f.close()

# element    = doc.GetElement(element_id)
#   surf = 0
print("*"*100)
print("Windows family :")
print("*"*100)
# Create a FilteredElementCollector to get all the windows
windows = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsNotElementType().ToElements()
#windows = FilteredElementCollector(doc).OfClass(window).WhereElement
TPWind  = 0
numWind = 0
# Loop through the windows and do something with them
for window in windows:
    # Do something with the wall, for example, print its name
    numWind += 1
    id  = window.Id
    element    = doc.GetElement(id)

    print("*"*10)
    print ("ID",id.IntegerValue )
    print("Name :",window.Name)
    print("UniqueId :",window.UniqueId)
    # print("Location :",window.Location.ToString)
    print("IsValidObject :",window.IsValidObject)
    print("IsTransient :",window.IsTransient )
    # print("Category :",window.Category)

    cons = element.Symbol.GetThermalProperties().AnalyticConstructionName
    u_val = element.Symbol.GetThermalProperties().HeatTransferCoefficient
    r_val = element.Symbol.GetThermalProperties().ThermalResistance
    vis = element.Symbol.GetThermalProperties().VisualLightTransmittance

    print ("It has Thermal Properties ?")
    print(element.Symbol.HasThermalProperties())
    print ("The construction gbXML name:",cons)
    print ("The transfer  coefficient value (U-Value):",u_val)
    print ("The thermal resistance value (R-Value): ",r_val)
    print ("The visual light transmittance: ",vis)

    param_set = window.Parameters
    # PRINT PARAMETER VALUES FOR THE SELECTED ELEMENT
    print("Parameter Values:")
    for param in param_set:
        print(param.Definition.Name, param.AsString(), param.AsValueString(), param.AsDouble())
        print("Storage type: ", param.StorageType, ", read only :", param.IsReadOnly)
        if (param.Definition.Name == "Surface"):
            surf = param.AsDouble()
    s = math.ceil(surf) / 10

    H = u_val * s
    print ("{} * {} = {} W/m².K".format(u_val, s, H))
    print ("le coefficient de déperdition = {} W/m².K ".format(H))

    print ("*** Calcul la puissance de chauffage (déperdition surfacique) \n θ (W) = H * ∆T")


    # En fixe à 20 °C la température résultante que les équipements de chauffage doivent permettre de maintenir au centre des pièces des logements
    Pch = H * (20 - Tex)
    print ("{} * (20 - {}) = {} W ".format(H, Tex, Pch))
    print ("la puissance de chauffage = {} W ".format(Pch))
    print ("-" * 10)
    TPWind += Pch
    print ("-" * 10)
    #La totale de puissance de chauffage des  fenetres
print ("The total heating power of the  {} windows = {}W".format(numWind ,TPWind))




