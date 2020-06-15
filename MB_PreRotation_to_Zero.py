# *- coding: utf-8 -*-　#UTF8宣言使えば日本語使える
from pyfbsdk import FBConstraintManager, FBObjectList, FBGetSelectedObjects

Objects = FBObjectList()
FBGetSelectedObjects(Objects)

for Object in Objects:
    print("Name = " + Object.Name)  #ObjectName
    RotDOF = Object.PropertyList.Find("RotationActive").Data  #Enable Rotation DOF
    print("RotDOF = " + str(RotDOF))
    LclRot=Object.PropertyList.Find("Lcl Rotation").Data #Lcl Rotation
    print("Lcl Rotation = " + str(LclRot))
    PreRot=Object.PropertyList.Find("PreRotation").Data #PreRotation
    print("PreRotatio = " + str(PreRot))
    
    AAA = LclRot + PreRot
    print (AAA)

print("終わり")
