# -*- coding : utf-8 -*-

#Import
from Autodesk.Revit.DB import *

#Variable
vidoc = __revit__.ActiveUIDocument
doc   = __revit__.ActiveUIDocument.Document

#Fun

def get_selected_elements(vidoc):
    """
    This function will return element that are currntly selected
    :param vidoc: vidoc where element are selected
    :return: List of selected elements
    """
    return  [ vidoc.Document.GetElement(elem_id) for elem_id in vidoc.Selection.GetElementIds() ]

