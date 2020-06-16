import re
from pyfbsdk import *
 
def get_find_objects_by_name(name, items):
    ptn = re.compile(name)
    result = []
    for item in items:
        if ptn.search(item.Name):
            result.append(item)
    return result
     
def print_names(comment, items):
    for item in items:
        print comment, item.Name
 
a = get_find_objects_by_name("", FBSystem().Scene.Groups)
print_names("Groups:", a)
a = get_find_objects_by_name("Position", FBSystem().Scene.Constraints)
print_names("Constraints:", a)
a = get_find_objects_by_name("^(?!Producer)", FBSystem().Scene.Cameras)
print_names("Cameras:", a)