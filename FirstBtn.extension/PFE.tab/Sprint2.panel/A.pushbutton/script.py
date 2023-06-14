__name__ = "Select element"
__title__ = "Get ID"
__doc__   = "Version 1.0"

# import os
# os.path.exist

import clr
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI.Selection import ObjectType

# Get the Revit application and document
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

# Get the current selection
selection = __revit__.ActiveUIDocument.Selection

# Prompt the user to select a wall
selected_element = selection.PickObject(ObjectType.Element, "Select an element ")

# Get the Element ID of the selected wall
element_id = selected_element.ElementId

element_type = selected_element

# Print the Element ID to the Revit Python Shell
print("Selected Element ID: {}".format(element_id))
