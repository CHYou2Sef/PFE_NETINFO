__title__ = "Hello"
__author__ = "Chebl Youssef"
__doc__ =   """
This is the first button ...
"""
#var
udoc = __revit__.ActiveUIDocument

#import
from  Snippets._selection import  get_selected_elements


if __name__ == '__main__':
    print("Hello youssef in Revit World !")
    print(get_selected_elements(udoc))
