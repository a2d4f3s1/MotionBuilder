# *- coding: utf-8 -*-　#UTF8宣言使えばMB内でも日本語使える
from pyfbsdk import FBConstraintManager, FBModelList, FBGetSelectedModels

Models = FBModelList()
FBGetSelectedModels(Models)

for Model in Models:
    print(Model.PropertyList.Find("Lcl Rotation").Data)  # Lcl Rotation
    print(Model.PropertyList.Find("RotationActive").Data)  # Enable Rotation DOF
    print(Model.PropertyList.Find("RotationOrder").Data)  # Rotation Order
    print(Model.PropertyList.Find("PreRotation").Data)  # Pre Rotation

print("終わり")
