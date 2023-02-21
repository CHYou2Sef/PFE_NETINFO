__title__ = "Test Tutorial"
__doc__   = "Version 1.0"

from Autodesk.Revit.DB import *
from pyrevit import  revit
import clr

#clr.AddReferrence('System')

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app = __revit__.Application

active_view = doc.ActiveView

all_room = FiltredElementCollector(doc).ofCategory(BuiltInCategory.OST_Rooms).ToElLements()
all_walls = FiltredElementCollector(doc).OfClass(Wall).WhereELementIsNotELementType().ToElLements()

all_doors = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereELementIsNotElementType().ToELements()
all_windows = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Windows).WhereELementIsNotElementType().ToElements()

all_views = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).WhereELementIsNotElementType().ToELements()

all_legends = [ view for view in all_views if view.ViewType == ViewType.Legend ]

print (len(all_views))
print (len(all_legends))

all_furn_in_view = FilteredElementCollector(doc, active_view.Id)\
                   .OfCategory(BuiltInCategory.O0ST_Furniture).WhereELementIsNotElementType().ToELements()

all_combined = list(all_rooms) + list(all_walls) + list(all_doors)
print(len(all_combined))

Categories = List [BuiltInCategory] ([BuiltInCategory.OST_Walls,
                                      BuiltInCategory.OST_Floors,
                                      BuiltInCategory.OST_Roofs,
                                      BuiltInCategory.OST_Ceilings])

custom_filter = ElementMulticategoryFilter(categories)
my_elements = FilteredElementCollector(doc).WherePasses(custom_filter).WhereELementIsElementType().ToELements()
print (my_elements)

