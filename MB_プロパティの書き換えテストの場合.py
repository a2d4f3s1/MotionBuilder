# *- coding: utf-8 -*-
from pyfbsdk import *
# ----------------------------------------------------------------------
# 書き換える場所
oClassName="FBModelNull" # テストしたいクラスの名前
oProperty="Show" # テストしたいプロパティ名
# ----------------------------------------------------------------------
 
# 全コンポーネントのリスト
lComps = FBSystem().Scene.Components
for lComp in lComps:
    if lComp.Selected==True:
        # リストの中から選択状態のものを取得
        if lComp.ClassName()==oClassName:
            # クラスの絞込み
            # プロパティの変更テスト
            for oPty in lComp.PropertyList:
                if oPty.Name==oProperty:
                    # 元々のプロパティの中身
                    print oPty.Data
# ----------------------------------------------------------------------
                    # 書き換える場所
                    # プロパティの書き換え
                    oPty.Data=True
# ----------------------------------------------------------------------