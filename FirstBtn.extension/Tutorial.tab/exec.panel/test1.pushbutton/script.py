__title__ = "Aff_Test 2"
__author__ = "Chebl Youssef"
__doc__ =   """
This is the first Test button Revit ...
"""
import clr
import os

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')


from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.IFC import *

uidoc = __revit__.ActiveUIDocument
doc = uidoc.Document

options = IFCFileReadOptions()
options.IncludeIFCSpaces = False
options.IncludeSiteElevation = False

ifc_file_path = os.path.join(os.path.dirname(__file__), 'test.txt')
ifc_importer = IFCImportOptions.CreateIFCImportOptions(doc, options)
imported_elements = IFCImportFile.Import(ifc_file_path, ifc_importer)

print(ifc_file_path)

print(len(imported_elements))

print(imported_elements)