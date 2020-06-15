from pyfbsdk import FBConstraintManager,FBModelList,FBGetSelectedModels

def getSelectedOrder():
    # selectionOrder selection order：セレクトオーダー
    # Get the current selection
    lModelList = FBModelList()
    pParent = None
    pSelected = True
    pSortSelectedOrder = True
    FBGetSelectedModels( lModelList, pParent, pSelected, pSortSelectedOrder )    
    
    if not lModelList: return None
    else: return lModelList
    
lSelected = getSelectedOrder()
#for i in range(len(lSelected)): print "%d: %s" % ( i, lSelected[i].Name )



result = []
for i in lSelected:
    #test_print
    #print i.Name

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


for num in range(0,len(result)-1):
    #親子付け
    result[num+1].Parent = result[num]