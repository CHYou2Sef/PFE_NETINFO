# # -*- coding: utf-8 -*-

__name__ = "Window Show data"
__title__ = "Window Param"

import os
os.path.exists

# Importation des modules requis
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import ObjectType
from urllib2 import request_host


# Definit le document actif
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# GET SELECTED ELEMENT
selection = uidoc.Selection
element_id = selection.PickObject(ObjectType.Element).ElementId
element = doc.GetElement(element_id)


# Recupere l element de la fentere
window = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).FirstElement()
# window = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereElementIsViewIndependent()
# print (window.Id)

print ("It has Thermal Properties ?")
print(window.HasThermalProperties())

# print (window)
# Rcupre les proprietes de transfert de chaleur et de resistance thermique
thermal_props = window.GetThermalProperties()
# print(thermal_props)
Struct_Section = window.GetStructuralSection()

# th_asset = window.GetThermalAsset()

Analyt  = thermal_props.AnalyticConstructionName
u_value = thermal_props.HeatTransferCoefficient
r_value = thermal_props.ThermalResistance
solar   = thermal_props.SolarHeatGainCoefficient
visual  = thermal_props.VisualLightTransmittance

# yest    = Struct_Section.NominalWeight

# mass    = thermal_props.ThermalMass
# rough   = thermal_props.Roughness
# Abso    = thermal_props.Absorptance
print ("The construction gbXML name. This value corresponds to the 'Name' property of a constructionType node in Constructions.xml:")
print (Analyt)
print ("The heat transfer coefficient value (U-Value). The unit is watts per meter-squared kelvin (W/(m^2*K)): ")
print (u_value)
print ("The calculated thermal resistance value (R-Value). The unit is meter-squared kelvin per watt ((m^2*K)/Watt): ")
print (r_value)
print ("The solar heat gain coefficient: ")
print (solar)
print ("The visual light transmittance: ")
print (visual)
# print ("\nThe calculated thermal mass value. The unit is kilogram feet-squared per second squared kelvin (kg ft^2/(s^2 K)):")
# print (mass)
# print ("\nValue of roughness: ")
# print (rough)
# print ("Value of absorptance: ")
# print (Abso)
# print (yest)
# Affiche les resultats dans une boite de dialogue
# TaskDialog.Show("Proprietes thermiques de la fenetre", "Coefficient de transfert de chaleur (U): {}\nResistance thermique (R): {}".format(u_value, r_value))
