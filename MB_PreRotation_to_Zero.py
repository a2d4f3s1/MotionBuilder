# *- coding: utf-8 -*-　#UTF8宣言使えば日本語使える
from pyfbsdk import FBConstraintManager, FBModelList, FBGetSelectedModels

Models = FBModelList()
FBGetSelectedModels(Models)

print("始まり\n")

for Model in Models:
    print ("Model Name = " + Model.Name)  #Model Name
    RotDOF = Model.PropertyList.Find("RotationActive")  #Enable Rotation DOF
    print ("Enable Rotation DOF = " + str(RotDOF.Data))
    LclRot=Model.PropertyList.Find("Lcl Rotation") #Lcl Rotation
    print ("Lcl Rotation = " + str(LclRot.Data))
    PreRot=Model.PropertyList.Find("PreRotation") #PreRotation
    print ("Pre Rotation = " + str(PreRot.Data))
    
    AddRot = LclRot.Data + PreRot.Data
    LclRot.Data=AddRot
    print ("\n" + Model.Name + " = " + str(LclRot))
    
    RotDOF.Data = False
    print ("Enable Rotation DOF = " + str(RotDOF.Data))

print("\n終わり")
