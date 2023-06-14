# import clr
# clr.AddReference('RevitAPI')
# clr.AddReference('RevitAPIUI')
# from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
#
# doc = __revit__.ActiveUIDocument.Document
#
# # Get all categories that can contain families
# categories = [cat for cat in doc.Settings.Categories if cat.AllowsBoundParameters]
#
# for category in categories:
#     # Get the category's built-in category id
#     bic = category.Id.IntegerValue
#
#     # Get all elements in the category that are families  :: WhereElementIsElementType()
#     collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory(bic)).WhereElementIsNotElementType()
#     families = [elem for elem in collector]
#
#     # Print the category name and number of families
#     print("{}: {}".format(category.Name, len(families)))
#
#     # Print the names of all families in the category
#     for family in families:
#         print("  {}".format(family.Name))

import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
from System import Enum

doc = __revit__.ActiveUIDocument.Document

# Get all categories that can contain families
categories = [cat for cat in doc.Settings.Categories if cat.AllowsBoundParameters]

for category in categories:
    # Get the category's built-in category id
    bic = category.Id.IntegerValue

    # Convert the integer value to the appropriate BuiltInCategory enumeration value
    category_enum = Enum.ToObject(BuiltInCategory, bic)

    # Get all elements in the category that are families :: WhereElementIsElementType()
    collector = FilteredElementCollector(doc).OfCategory(category_enum).WhereElementIsNotElementType()
    families = [elem for elem in collector]

    # Print the category name and number of families
    print("{}: {}".format(category.Name, len(families)))

    # Print the names of all families in the category
    for family in families:
        print("  {}".format(family))
