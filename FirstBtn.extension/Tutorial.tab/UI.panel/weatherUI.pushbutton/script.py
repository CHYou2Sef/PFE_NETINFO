# -*- coding: utf-8 -*-

import os
os.path.exists

import sqlite3
import sqlalchemy

from itertools import count

from rpw.utils.dotnet import Enum
from rpw.ui.forms.resources import *

from rpw.ui.forms import (FlexForm, Label, ComboBox, TextBox,Separator, Button, CheckBox)

#import data
f = open("C:\Users\YOUSSEF\PFE\Parameters.txt", "r")

Id = "ID : " + f.readline()
name  = "Name : " +  f.readline()
lat   = "Latitude : " + f.readline()
longi = "Longitude : " + f.readline()
temp  = "Temperature average : " +f.readline()+" °C"
hum   = "Humidity average : " + f.readline() +" %"
wind  = "Wind average : " +  f.readline() +" metre/sec"
cloud = "Cloud average : " + f.readline() +" %"
perci = "Precipitation average : "+ f.readline() +" %"

f.close()

if __name__ == '__main__':
    """ TESTS """
    components = [
                  Label('Averge Parameters :'),
                  Separator(),
                  ComboBox("combobox1", {"ID"       : Id  ,
                                          "Name"    : name,
                                          "Latitude"  : lat,
                                          "Longitude" : longi  ,
                                          "Temperature" : temp,
                                          "Humidity"    : hum,
                                          "Wind"  : wind,
                                          "Cloud" : cloud ,
                                          "Precipitation" : perci
                                         }),

                  #Label('Enter Name:'),
                  #TextBox('ch1', Text="Metric Value"),
                  CheckBox('checkbox1', 'Metric Value'),
                  Separator(),
                  Label("NB :"  ),Label("This was a result for api and other code python that does not work in pyrevit"  ),
                  Separator(),
                  Button('OK')]

    form = FlexForm('Weather Parameters', components)
    form.show()

    if 1 == "checkbox1":
        print(form.values , "(With metric values)")
    else:
        print(form.values , "(Without metric values)")




#**************
# from pyrevit import forms
#
# # ask user to enter their name
# name = forms.ask_for_string(prompt="Enter your name:")
# dd =forms.ask_for_list
#
# # ask user to select an option from the dropdown menu
# options = ["Option A", "Option B", "Option C"]
# selected_option = forms.ask_user_to_select_from_list(options, "Select an option:")
#
# # show a message box with the user input
# forms.alert("Hello, " + name + "! You selected " + selected_option + "." , ok=True)
# //////////////////////////////////////////
#
# from pyrevit import forms
#
# # prompt the user to enter their name
# name = forms.ask_for_string("Enter your name")
#
# # create a dialog box with the user's name
# forms.alert("Hello, {}".format(name))
#
# import rpw
# from Autodesk.Revit.UI import *
#
# # define a function to create the form
# def create_form(sender, args):
#     # create a new window
#     window = RevitTaskDialog("Example Form")
#
#     # add some input fields to the window
#     window.AddCommandLink(TaskDialogCommandLinkId.CommandLink1, "Option 1")
#     window.AddCommandLink(TaskDialogCommandLinkId.CommandLink2, "Option 2")
#     window.AddCommandLink(TaskDialogCommandLinkId.CommandLink3, "Option 3")
#
#     # show the window and get the result
#     result = window.Show()
#
#     # do something based on the result
#     if result == TaskDialogResult.CommandLink1:
#         rpw.ui.forms.Alert("You selected Option 1")
#     elif result == TaskDialogResult.CommandLink2:
#         rpw.ui.forms.Alert("You selected Option 2")
#     elif result == TaskDialogResult.CommandLink3:
#         rpw.ui.forms.Alert("You selected Option 3")
#
# # attach the create_form function to an event
# UiApplication = rpw.ui.Application()
# UiApplication.create_form = create_form
# UiApplication.start()




# ##-----------------------------------------------------
# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import *
#
# # Define a function that returns the current Revit version
# def revit_version():
#     uiapp = __revit__.Application
#     version = uiapp.Application.VersionName
#     return int(version[:4])
#
# # Define a function that creates an image instance based on the Revit version
# def create_image_instance(document, view, element_id, image_options):
#     version = revit_version()
#     if version >= 2020:
#         return ImageInstance.Create(document, view, element_id, image_options)
#     else:
#         # For older versions, use the deprecated method CreateImage
#         return document.CreateImage(view, element_id, image_options)
#
# # Example usage
# doc = __revit__.ActiveUIDocument.Document
# view = doc.ActiveView
# element_id = ElementId(1234)
# placement_options = ImagePlacementOptions()
# image_instance = create_image_instance(doc, view, element_id, placement_options)


#***************************************

# from pyrevit import forms
#
# # create a form with two input fields
# form = forms.WPFWindow(title="Example Form", width=300, height=200)
# lbl_name = forms.WPFLabel(content="Name:", font_weight="bold", margin="10,10,0,0")
# txt_name = forms.WPFTextBox(text="Enter your name", margin="10,35,0,0")
# lbl_email = forms.WPFLabel(content="Email:", font_weight="bold", margin="10,70,0,0")
# txt_email = forms.WPFTextBox(text="Enter your email", margin="10,95,0,0")
# btn_submit = forms.WPFButton(content="Submit", margin="120,140,0,0", width=80, height=30)
#
# # add the input fields and button to the form
# form.content = [lbl_name, txt_name, lbl_email, txt_email, btn_submit]
#
# # define a function to handle the button click event
# def submit_form(sender, args):
#     name = txt_name.Text
#     email = txt_email.Text
#     forms.alert("Thanks, {}! We'll be in touch at {}".format(name, email))
#
# # attach the submit_form function to the button click event
# btn_submit.Click += submit_form
#
# # show the form
# form.show()

#/////////////////////////
# import clr
# import Autodesk.Revit.UI
# from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons , TaskDialogCommandLinkId
# from Autodesk.Revit.UI.Selection import ObjectType
# from Autodesk.Revit.UI import *
#
#
# # Get the Revit application and document objects
# app = __revit__.Application
# doc = __revit__.ActiveUIDocument.Document
#
# # Define a function to be called when the button is clicked
# def button_clicked(sender, args):
#     # Get the value of the text field
#     text = sender.GetTextBox().Value
#     # Show a message box with the value of the text field
#     TaskDialog.Show('My UI', text)
#
# # Create a simple form with a text field and a button
# form = Autodesk.Revit.UI.TaskDialog('My UI')
# form.MainInstruction = 'Enter some text:'
# form.CommonButtons = TaskDialogCommonButtons.Ok
# # form.AddCommandLink(ObjectType.Element, 'Submit')
# form.AddCommandLink(TaskDialogCommandLinkId.CommandLink1,"sub")
#
# text_box = Autodesk.Revit.UI.TextBox()
# text_box.PromptText = 'hello world'
# form.SetTextBox(text_box)
#
# # Add the button event handler
# form.CommandLinkClicked += button_clicked
#
# # Show the form
# form.Show()

#/////////////////////////////////////////

#
# import clr
# import sys
# import os
#
# # Add the PyRevit IronPython library to the search path
# pyrevit_path = os.path.join(os.environ["APPDATA"], "C:\Users\YOUSSEF\AppData\Roaming\pyRevit-Master")
# clr.AddReferenceToFileAndPath(os.path.join(pyrevit_path,"pyrevitlib.dll"))
#
# # Add the Revit API and DB references
# clr.AddReference("RevitAPI")
# clr.AddReference("RevitAPIUI")
#
# # Import the required classes and modules
# from Autodesk.Revit.UI import TaskDialog, TaskDialogCommonButtons
# from System import Uri, IO
# from pyrevit import script, output
#
# # Create a new Revit Task Dialog and set its title and main instruction
# dialog = TaskDialog("My PyRevit UI")
# dialog.MainInstruction = "Welcome to my PyRevit UI!"
#
# # Set an image for the title of the dialog
# image_path = r"Y:\photo\561492.png"
# if not IO.File.Exists(image_path):
#     output.warning("Image not found at {}".format(image_path))
# else:
#     dialog.TitleIcon = Uri(image_path)
#
# # Add a custom command link to the dialog
# command_name = "My PyRevit Command"
# command_description = "Click this button to run the command"
# command_link = dialog.AddCommandLink(TaskDialogCommonButtons.Yes, command_name)
# dialog.CommonButtons = TaskDialogCommonButtons.Close
#
# # Show the dialog and get the result
# result = dialog.Show()
#
# # Check the result of the dialog
# if result == TaskDialogCommonButtons.Close:
#     script.exit()
# elif result == command_name:
#     # Perform the desired action for the custom command link
#     output.print_md("You clicked the '{}' button!".format(command_name))
#

#
# # Import required PyRevit modules
# from pyrevit import revit, DB
# from pyrevit import forms
# from pyrevit import script
# from pyrevit import output
# from pyrevit import UI
#
#
#
# # Create a new Revit Task Dialog and set its title and main instruction
# dialog = forms.TaskDialog("My PyRevit UI")
# dialog.MainInstruction = "Welcome to my PyRevit UI!"
#
# # Set an image for the title of the dialog
# image_path = r"Y:\photo\561492.png"
# if not System.IO.File.Exists(image_path):
#     output.warning("Image not found at {}".format(image_path))
# else:
#     dialog.TitleImage = UI.Image.from_file(image_path)
#
# # Add a custom command link to the dialog
# command_name = "My PyRevit Command"
# command_description = "Click this button to run the command"
# command_link = forms.CommandLink(command_name, command_description)
# dialog.AddCommandLink(command_link)
#
# # Show the dialog and get the result
# result = dialog.Show()
#
# # Check the result of the dialog
# if result == forms.DialogResult.Cancel:
#     script.exit()
# elif result == command_name:
#     # Perform the desired action for the custom command link
#     output.print_md("You clicked the '{}' button!".format(command_name))
#
#
#

#
# __title__ = "Weather UI"
# __author__ = "Chebl Youssef"
# __doc__ =   """
# This is the first Version ...
# """
#
# import clr
# clr.AddReference('RevitAPI')
# clr.AddReference('RevitAPIUI')
#
# from Autodesk.Revit.DB import *
#
# from System.Drawing import *
#
# import System.Drawing
# import System.Windows.Forms
#
# from System.Drawing import *
# from System.Windows.Forms import *
#
#
# class Form1(Form):
#     def __init__(self):
#         self.InitializeComponent()
#
#     def InitializeComponent(self):
#         resources = System.Resources.ResourceManager("Form1", System.Reflection.Assembly.GetEntryAssembly())
#         self._groupBox1 = System.Windows.Forms.GroupBox()
#         self._groupBox2 = System.Windows.Forms.GroupBox()
#         self._pictureBox1 = System.Windows.Forms.PictureBox()
#         self._textBox1 = System.Windows.Forms.TextBox()
#         self._pictureBox1.BeginInit()
#         self.SuspendLayout()
#         #
#         # groupBox1
#         #
#         self._groupBox1.Location = System.Drawing.Point(12, 289)
#         self._groupBox1.Name = "groupBox1"
#         self._groupBox1.Size = System.Drawing.Size(317, 155)
#         self._groupBox1.TabIndex = 0
#         self._groupBox1.TabStop = False
#         self._groupBox1.Text = "groupBox1"
#         #
#         # groupBox2
#         #
#         self._groupBox2.Location = System.Drawing.Point(347, 289)
#         self._groupBox2.Name = "groupBox2"
#         self._groupBox2.Size = System.Drawing.Size(316, 155)
#         self._groupBox2.TabIndex = 1
#         self._groupBox2.TabStop = False
#         self._groupBox2.Text = "groupBox2"
#         #
#         # pictureBox1
#         #
#         self._pictureBox1.Image = resources.GetObject("pictureBox1.Image")
#         self._pictureBox1.Location = System.Drawing.Point(12, 49)
#         self._pictureBox1.Name = "pictureBox1"
#         self._pictureBox1.Size = System.Drawing.Size(651, 222)
#         self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
#         self._pictureBox1.TabIndex = 2
#         self._pictureBox1.TabStop = False
#         #
#         # textBox1
#         #
#         self._textBox1.AccessibleDescription = "Current Weather"
#         self._textBox1.AccessibleName = "wTitle"
#         self._textBox1.AccessibleRole = System.Windows.Forms.AccessibleRole.TitleBar
#         self._textBox1.BackColor = System.Drawing.SystemColors.Control
#         self._textBox1.Font = System.Drawing.Font("Sitka Subheading", 48,
#                                                   System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic,
#                                                   System.Drawing.GraphicsUnit.Point, 0)
#         self._textBox1.Location = System.Drawing.Point(12, 12)
#         self._textBox1.Name = "textBox1"
#         self._textBox1.ReadOnly = True
#         self._textBox1.Size = System.Drawing.Size(651, 108)
#         self._textBox1.TabIndex = 3
#         self._textBox1.Text = "Current Weather"
#         #
#         # Form1
#         #
#         self.ClientSize = System.Drawing.Size(675, 456)
#         self.Controls.Add(self._textBox1)
#         self.Controls.Add(self._pictureBox1)
#         self.Controls.Add(self._groupBox2)
#         self.Controls.Add(self._groupBox1)
#         self.Name = "Form1"
#         self.Text = "Form1"
#         self._pictureBox1.EndInit()
#         self.ResumeLayout(False)
#         self.PerformLayout()
#
#

