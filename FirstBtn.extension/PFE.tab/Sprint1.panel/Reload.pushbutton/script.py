# -*- coding: utf-8 -*-

__name__ = "Location"
__title__ = "Reload"

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

res = True

def display_alert():
    # Check if the active document is valid
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
            MessageBox.Show("The latitude and longitude of the project site are :\n" + str(lat) + " , " + str(lon) + "\nYour project location is in "+ str(pl)
                            +"\nIf you want to change it go to toolbar :\n>> Manage >> Location ", "Revit Project Location")
    else:
        # Active document is not valid
        MessageBox.Show("There is no active document open", "Revit Project Location")


# Define the function to display the alert after 5 seconds
def delayed_alert():
    # Wait for 5 seconds
    System.Threading.Thread.CurrentThread.Join(5000)
    # Display the alert
    display_alert()

if EXEC_PARAMS.executed_from_ui:
    # Call the delayed_alert function after Revit is initialized
    res = forms.alert("Are you sure you want to reload ?",ok=False, yes=True, no=True)

if res:
    logger = script.get_logger()
    results = script.get_results()

    # re-load pyrevit session.
    logger.info('Reloading....')
    sessionmgr.reload_pyrevit()

    results.newsession = sessioninfo.get_session_uuid()

    delayed_alert()



