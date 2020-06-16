# *- coding: utf-8 -*-
from pyfbsdk import *
# 全コンポーネントのリスト
lComps = FBSystem().Scene.Components
for lComp in lComps:
    if lComp.Selected==True:
        # リストの中から選択状態のものを取得
        print "----------------------------------------------------------"
        print lComp.LongName
        print lComp.ClassName()
        # 選択ノードのプロパティリストを取得
        lPtys=lComp.PropertyList
        print "<Property>"
        for oPty in lPtys:
            print "\t" + oPty.Name
        # 選択ノードに組み込まれてるファンクション,アトリビュートを取得
        Dirs=dir(lComp)
        print "<dir>"
        for oDir in Dirs:
            print "\t" + oDir