# -*- coding: utf-8 -*-

__name__ = "Localisation"
__title__ = "Location"

import os
os.path.exists

from pyrevit import revit, EXEC_PARAMS , script , forms
from pyrevit.loader import sessionmgr
from pyrevit.loader import sessioninfo

import clr
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import MessageBox
import System
import System.Threading


if revit.doc:
    # Get the site location of the current document
    siteLoc = revit.doc.SiteLocation
    if siteLoc is None:
        # Site location is not defined
        MessageBox.Show("The site location is not defined for this project", "Revit Project Location")
    else:
        # Get the latitude and longitude of the site location
        lat = siteLoc.Latitude * 57.25
        lon = siteLoc.Longitude * 57.35
        pl = siteLoc.PlaceName
        #print ( ppl)
        # Show a message box with the location
        print("The latitude and the longitude of the project site are : {} , {} \nYour project location is in {} . \nIf you want to change it go to toolbar : >> Manage >> Location ".format(str(lat),  str(lon),  str(pl)))
else:
    # Active document is not valid
    MessageBox.Show("There is no active document open", "Revit Project Location")
