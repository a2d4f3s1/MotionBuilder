# *- coding: utf-8 -*-　#UTF8宣言使えば日本語使える
from pyfbsdk import FBConstraintManager, FBModelList, FBGetSelectedModels

Models = FBModelList()
FBGetSelectedModels(Models)

count = 0
print("----- DOF Disable 処理開始 -----\n")

for Model in Models:
    print(count)
    print("Model Name = " + Model.Name)  # Model Name
    if Model.Rotation.GetAnimationNode() is None:  # アニメーションが無い
        RotDOF = Model.PropertyList.Find("RotationActive")  # Enable Rotation DOF
        if RotDOF.Data is True:
            LclRot = Model.PropertyList.Find("Lcl Rotation")  # Lcl Rotation
            print("Lcl Rotation = " + str(LclRot.Data))
            PreRot = Model.PropertyList.Find("PreRotation")  # PreRotation
            print("Pre Rotation = " + str(PreRot.Data))
            print("LclRotationを更新、DOFを無効化します")
            AddRot = LclRot.Data + PreRot.Data  # ただの足し算、、、バグったらたぶんここ
            LclRot.Data = AddRot
            print("Lcl Rotation = " + str(LclRot.Data))
            RotDOF.Data = False
            print("Enable Rotation DOF = " + str(RotDOF.Data))
        else:
            print("DOFは無効です")
    else:
        print("Rotationのアニメーションが有効です\n")
    count = count + 1

print("----- DOF Disable 処理完了 -----")
