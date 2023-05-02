# -*- coding: utf-8 -*-
__title__ = "Revit Parameters"
__doc__   = "Version 1.0"

###########################
#import
###########################

from Autodesk.Revit.DB import *

###########################
#var
###########################

doc   = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app   = __revit__.Application

###########################
#main
###########################

#get wall
print('*'*50)

# Get selected items in document
# selection = uidoc.Selection.GetElementIds()

# # Prompt the user to select a wall
# selected_wall = selection.PickObject(ObjectType.Element, "Select a wall")
#
# # Get the Element ID of the selected wall
wall_id = ElementId(428745)

wall    = doc.GetElement(wall_id)
#wall    = doc.GetElement(428745)

#print(wall)
#print(list(wall.Parameters))

###########################
#parameters
###########################


#print('*'*50)
#print("*** Parameters : ***")
# for p in wall.Parameters :
#     # if p.Definition.Name == 'Comments':  #don't use this
#     #     print ("its a comments")
#     #     print(p.Id)
#
#     print(p)
#     print('.Name :             {}'.format(p.Definition.Name))
#     print('.BuiltInParameter : {}'.format(p.Definition.BuiltInParameter))
#     print('.StorageType :      {}'.format(p.StorageType))
#     print('.IsShared :         {}'.format(p.IsShared))
#     print('.IsReadOnly :       {}'.format(p.IsReadOnly))
#     print("-"*10)

############################
#Get Built in parameters
############################
#
# print('*'*50)
# print("*** Built In Parameters : ***")
# wall_comments = wall.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
# wall_type_name = wall.get_Parameter(BuiltInParameter.ELEM_TYPE_PARAM)
#
# print('.Name :             {}'.format(wall_comments.Definition.Name))
# print('.BuiltInParameter : {}'.format(wall_comments.Definition.BuiltInParameter))
# print('.StorageType :      {}'.format(wall_comments.StorageType))
# print('.IsShared :         {}'.format(wall_comments.IsShared))
# print('.IsReadOnly :       {}'.format(wall_comments.IsReadOnly))
# print("-"*10)
#
# print(wall_comments.AsValueString())
# print(wall_comments.AsDouble())
# print(wall_type_name.AsString())
# print(wall_type_name.AsValueString())


###########################
#Get  parameters  by name
###########################
# print('*'*50)
# print("*** Get  Parameters By Name : ***")
#
# suface =wall.LookupParameter("Surface")
# print('Surface en d/f  : {} '.format(suface.AsDouble()))
# print("Surface element : ",suface.Element())

# ********* Dosen't work *************
#cat = wall.LookupParameter("category")
#print ("Type de category : {} ".format(cat))
#
# fam  = wall.LookupParameter("sp_material").AsElementId()
# fam_id = doc.GetElement(fam)
# print ("La famille : {} ".format(fam_id.Name))
# ***************************************

###########################
#Get  Type parameters
###########################
#
# print('*'*50)
# print("*** Get Type  Parameters  : ***")
#
# wall_type      = wall.WallType
# wall_type_name = wall_type.get_Parameter(BuiltInParameter.MATERIAL_NAME)
# wall_type_desc = wall_type.get_Parameter(BuiltInParameter.ALL_MODEL_DESCRIPTION)
# wall_type_mark = wall_type.get_Parameter(BuiltInParameter.ALL_MODEL_TYPE_MARK)
#
#
# print (wall_type)
# print (wall_type_name)
# print (wall_type_desc.AsString())
# print (wall_type_mark.AsString())


###########################
# SET  parameter  Value
###########################

print('*'*50)
print("*** Set  Parameters Value : ***")

wall_comments = wall.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)

print(wall_comments.AsString())
#print(wall_comments.AsDouble())

t = Transaction(doc , __title__)
t.Start()

wall_comments.Set("What is This ...")
print(wall_comments.AsString())

t.Commit()

###########################
# Costum tool
###########################

t = Transaction(doc , "write ids to mark param of walls ")
t.Start()

# SET WALL ELEMENT-ID TO MARK
all_walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

for wall in all_walls:
    wall_mark = wall.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
    wall_coast = wall.get_Parameter(BuiltInParameter.ALL_MODEL_COST)

    wall_mark.Set(str(wall.Id))
    # print(wall.Id)
    print ("Coast :",wall_coast)

t.Commit()
print ("This is my keyboard hhh ")
