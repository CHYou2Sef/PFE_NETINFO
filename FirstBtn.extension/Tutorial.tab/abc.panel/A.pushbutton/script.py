__name__ = "Select element"
__title__ = "select wall"
__doc__   = "Version 1.0"

import clr
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI.Selection import ObjectType

# Get the Revit application and document
app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

# Get the current selection
selection = __revit__.ActiveUIDocument.Selection

# Prompt the user to select a wall
selected_wall = selection.PickObject(ObjectType.Element, "Select a wall")

# Get the Element ID of the selected wall
wall_id = selected_wall.ElementId

# Print the Element ID to the Revit Python Shell
print("Selected wall ID: {}".format(wall_id))
