import clr
from Autodesk.Revit.DB import BuiltInCategory
from Autodesk.Revit.DB import FilteredElementCollector

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

from Autodesk.Revit.DB import *

# Get the active Revit document
doc = __revit__.ActiveUIDocument.Document
# Get the material to apply to the walls
#material_name = "Brick"
material = None
materials_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Materials).WhereElementIsNotElementType()
for mat in materials_collector:
	print(mat.Name)
	#if mat.Name == material_name:
		#material = mat
		#break
#if not material:
    #raise Exception(f"Material '{material_name}' not found")
