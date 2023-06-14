# -*- coding: utf-8 -*-
__name__ = "Show Element Data"
__title__ = 'Element Info'
__author__ = 'Chebl Youssef'

### ∞~∝≅≈∄∃∇℃℉°%∅∩∪√∂∁∀≡θεγβα↔∋ϑμπρστφω*Ωφ

import os
os.path.exists

import math

# Importation des modules requis
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import ObjectType

# Definit le document actif
doc   = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# GET SELECTED ELEMENT
selection  = uidoc.Selection
element_id = selection.PickObject(ObjectType.Element).ElementId
element    = doc.GetElement(element_id)
print("------------------------------")
print("1 :", element_id)
print("2 :", element_id.IntegerValue)
print("3 :", element.Category.Id)
#print("3 :", element)

print("------------------------------")
f = open("C:\\Users\\YOUSSEF\\PFE\\Temp.txt", "r")
Tex = float(f.read())
f.close()
param_set = element.Parameters
# PRINT PARAMETER VALUES FOR THE SELECTED ELEMENT
print("Parameter Values:")
for param in param_set:
    print(param.Definition.Name,  param.AsString(), param.AsValueString(),  param.AsDouble())
    print("Storage type: ", param.StorageType.ToString(), ", read only :", param.IsReadOnly)
    print ("-" * 10)
    if (param.Definition.Name == "Surface") : sur = param.AsDouble()
s = math.ceil(sur) / 10

print ("It This element has Thermal Properties ?")
if element.Symbol.HasThermalProperties() == True :
    print("A: ",element.Symbol.HasThermalProperties())

    thermal_props = element.Symbol.GetThermalProperties()
    u_val = thermal_props.HeatTransferCoefficient

    print("*"*10)
    print ("Bilan thermique")
    # Calcul la puissance de chauffage (déperdition surfacique)
    print ("***Calculation of heating power (area loss) \n θ (W) = H * ∆T")
    print ("Surface = {} m²".format(s))
    print ("U = {} W/(m²/K)".format(u_val))

    H = u_val * s
    print ("{} * {} = {} W/m².K".format(u_val, s, H))
    # le coefficient de déperdition
    print ("= {} W/m².K ".format(H))

    # En fixe à 20 °C la température résultante que les équipements de chauffage doivent permettre de maintenir au centre des pièces des logements
    print ("By fixing the indoor temperature at 20°C and outdoor at {}°C".format(Tex))
    Pch = H * (20 - Tex)
    print ("{} * (20 - {}) = {} W ".format(H, Tex, Pch))
    # la puissance de chauffage
    print ("the heating power of ''{}'' = {} W ".format(element.Name, Pch))

else:
    print ("This element has not Thermal Properties ...")
