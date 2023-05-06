# -*- coding: utf-8 -*-

__title__ = 'Select a window'
__author__ = 'Chebl Youssef'

"""Windows Select and show infomation..."""

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
print (element.Category.Id)
print("3 :", element)

print("------------------------------")

if element.Category.Name == "Fenêtres":
    param_set = element.Parameters


    Length            = element.get_Parameter(BuiltInParameter.FABRICATION_PART_LENGTH)
    width             = element.get_Parameter(BuiltInParameter.WINDOW_WIDTH)
    height            = element.get_Parameter(BuiltInParameter.WINDOW_HEIGHT)
    Window_Area       = element.get_Parameter(BuiltInParameter.RBS_HVACLOAD_WINDOW_AREA_PARAM)
    Mass_window       = element.get_Parameter(BuiltInParameter.MASS_DATA_MASS_WINDOW_AREA)
    thikness          = element.get_Parameter(BuiltInParameter.WINDOW_THICKNESS)
    Construction_Type = element.get_Parameter(BuiltInParameter.WINDOW_CONSTRUCTION_TYPE)

    #aaa = element.get_Parameter(FamilySymbol.Activate())

    # vol   = element.LookupParameter("Volume")
    vol = element.GetMaterialVolume(element_id)
    vol2 = element.GetParameters("Volume")
    #vol2  = element.ParameterSet.Size.Width


    cons  = element.Symbol.GetThermalProperties().AnalyticConstructionName
    u_val = element.Symbol.GetThermalProperties().HeatTransferCoefficient
    r_val = element.Symbol.GetThermalProperties().ThermalResistance
    vis   = element.Symbol.GetThermalProperties().VisualLightTransmittance
    # PRINT BUILT-IN PARAMETERS FOR THE SELECTED ELEMENT
    print("Selected Element ID:", element_id.IntegerValue)
    print("------------------------------")
    print("Element Name:", element.Name)
    print ("Symbol Name",element.Symbol.Family.Name)
    print("Element Category Name :", element.Category.Name)

    print ("It has Thermal Properties ?")
    print(element.Symbol.HasThermalProperties())
    print ("The construction gbXML name:",cons)
    print ("The transfer  coefficient value (U-Value):",u_val)
    print ("The thermal resistance value (R-Value): ",r_val)
    print ("The visual light transmittance: ",vis)
    print ("The volume (Returns 0.0 if the material is not a part of this element): ",vol)
    print ("The width",width.AsValueString())
    print ("The height: ",height.AsValueString())
    surface = width.AsDouble() * height.AsDouble()
    print ("The volume calculated: ",surface)
    print ("The volume calculated 2 : ",vol2)
    print ("Window Area" ,Window_Area)
    print ("Mass Window Area",Mass_window)
    print ("Window Length" ,Length)
    print ("Window thikness" ,thikness)
    print ("Window Construction Type" ,Construction_Type)
    print ("-"*10)
    print("Window Width:", element.get_Parameter(BuiltInParameter.WINDOW_WIDTH).AsValueString())
    print("Window Height:", element.get_Parameter(BuiltInParameter.WINDOW_HEIGHT).AsValueString())
    print("Window Area:", element.get_Parameter(BuiltInParameter.HOST_AREA_COMPUTED).AsValueString())
    print("Window Volume:", element.get_Parameter(BuiltInParameter.HOST_VOLUME_COMPUTED).AsValueString())

    # PRINT PARAMETER VALUES FOR THE SELECTED ELEMENT
    print("Parameter Values:")
    for param in param_set:
        print(param.Definition.Name,  param.AsString(), param.AsValueString(),  param.AsDouble())
        print("Storage type: ", param.StorageType, ", read only :", param.IsReadOnly)
        print ("-" * 10)
        if (param.Definition.Name == "Surface") : sur = param.AsDouble()

    # print ("It Can have Structural section ?")
    # print(element.Symbol.CanHaveStructuralSection())
    # print("Element Mark:", element.get_Parameter(BuiltInParameter.ALL_MODEL_MARK).AsValueString())
    # print("Element Cost:", element.get_Parameter(BuiltInParameter.WINDOW_CONSTRUCTION_TYPE))
    # print("Element Width:", element.get_Parameter(BuiltInParameter.WINDOW_WIDTH))
    # print("Element Height:", element.get_Parameter(BuiltInParameter.WINDOW_HEIGHT))
    s = math.ceil(sur) / 10

    print("*"*10)
    print ("Bilan thermique")
    print ("5. Calcul le coefficient de déperdition H (W/m².K) \n H = U * Surface ")

    H = u_val * s
    print ("{} * {} = {} W/m².K".format(u_val,s,H ))

    print ("le coefficient de déperdition = {} W/m².K ".format(H))

    ### ∞~∝≅≈∄∃∇℃℉°%∅∩∪√∂∁∀≡θεγβα↔∋ϑμπρστφω*Ωφ
    print ("*** Calcul la puissance de chauffage (déperdition surfacique) \n θ (W) = H * ∆T")

    Tex = 17
    # En fixe à 20 °C la température résultante que les équipements de chauffage doivent permettre de maintenir au centre des pièces des logements
    Pch = H * (20 - Tex)

    print ("{} * (20 - {}) = {} W ".format(H, Tex, Pch))
    print ("la puissance de chauffage de {} = {} W ".format(element.Name,Pch))

else:
    print("Selected element is not a window.")
