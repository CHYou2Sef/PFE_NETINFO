import pyrevit
from pyrevit import revit, DB

# retrieve project information
doc = revit.doc
project_info = doc.ProjectInformation

# retrieve and format project start and end dates
start_date = project_info.get_Parameter(DB.BuiltInParameter.PROJECT_START_DATE).AsValueString()
end_date = project_info.get_Parameter(DB.BuiltInParameter.PROJECT_END_DATE).AsValueString()

# print project properties
print("Project Name:", project_info.Name)
print("Project Number:", project_info.get_Parameter(DB.BuiltInParameter.PROJECT_NUMBER).AsString())
print("Project Address:", project_info.get_Parameter(DB.BuiltInParameter.PROJECT_ADDRESS).AsString())
print("Project Status:", project_info.Status)
print("Project Start Date:", start_date)
print("Project End Date:", end_date)
