from pyfbsdk import FBConstraintManager, FBModelList, FBGetSelectedModels

Models = FBModelList()
FBGetSelectedModels(Models)

for Model in Models:
    print(Model.Name)

print("END")
