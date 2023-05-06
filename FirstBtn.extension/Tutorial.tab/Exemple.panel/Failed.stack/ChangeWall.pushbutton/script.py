# -*- coding: utf-8 -*-
__name__ = "Change element "
__title__ = "change selected wall"
__doc__   = "Version 0.1"

import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.UI.Selection import ObjectType
from Autodesk.Revit.DB import *

doc       = __revit__.ActiveUIDocument.Document
uidoc     = __revit__.ActiveUIDocument

#selection = __revit__.ActiveUIDocument.Selection
selection = uidoc.Selection.GetElementIds()


# Prompt the user to select a wall
#selected_wall = selection.PickObject(ObjectType.Element, "Select a wall")

# Get the Element ID of the selected wall
#wall_id = selected_wall.ElementId
#print (wall_id)

#Selected element
if len(selection) != 1:
    raise Exception("Select a wall.")

# Get selected item
selected_wall = doc.GetElement(selection.First())

# Change the material of the selected wall
t = Transaction(doc, __title__)
t.Start()

material_id = ElementId(849032) # Replace with the desired material ID
print (material_id)

selected_wall.Parameter[BuiltInParameter.WALL_STRUCTURAL_SIGNIFICANT].Set(material_id)

t.Commit()

