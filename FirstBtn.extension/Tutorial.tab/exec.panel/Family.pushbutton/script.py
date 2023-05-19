import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = __revit__.ActiveUIDocument.Document

# Get all categories that can contain families
categories = [cat for cat in doc.Settings.Categories if cat.AllowsBoundParameters]

for category in categories:
    # Get the category's built-in category id
    bic = category.Id.IntegerValue

    # Get all elements in the category that are families
    collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory(bic)).WhereElementIsElementType()
    families = [elem for elem in collector]

    # Print the category name and number of families
    print("{}: {}".format(category.Name, len(families)))

    # Print the names of all families in the category
    for family in families:
        print("  {}".format(family.Name))
