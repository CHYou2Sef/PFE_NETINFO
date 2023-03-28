import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# Récupérer les éléments sélectionnés dans le document
selection = uidoc.Selection.GetElementIds()

# Prompt the user to select a wall
selected_wall = selection.PickObject(ObjectType.Element, "Select a wall")

# Get the Element ID of the selected wall
wall_id = selected_wall.ElementId

# Vérifier si un élément a été sélectionné
if len(selection) != 1:
    raise Exception('Sélectionnez un mur.')

# Récupérer l'élément sélectionné
selected_wall = doc.GetElement(selection.First())

# Changer le matériau du mur sélectionné
t = Transaction(doc, 'Changer le matériau du mur')
t.Start()

material_id = ElementId(wall_id) # Remplacer 123456 par l'ID du matériau souhaité
selected_wall.Parameter[BuiltInParameter.WALL_STRUCTURAL_SIGNIFICANT].Set(material_id)

t.Commit()
