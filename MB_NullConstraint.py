from pyfbsdk import FBConstraintManager,FBModelList,FBGetSelectedModels

models = FBModelList()
FBGetSelectedModels(models)


result = []
for i in models:
    print i.Name

    #ヌルの生成
    pSrcObj = FBModelNull("SourceNull")
    pSrcObj.Show = True

    result.append(pSrcObj)

    #コンストレイント
    CM = FBConstraintManager()
    c = CM.TypeCreateConstraint(3)
    #コンストイント内名前検索
    PropertyName = "Source (Parent)"

    #models = FBModelList()
    #FBGetSelectedModels(models)
    #つまり i

    #コンストレイント処理
    c.PropertyList.Find(PropertyName).append(i)
    c.ReferenceAdd(0,pSrcObj)

    c.Active = True
    c.Lock = True

print result
