#coding: utf-8

#TODO ドキュメンテーション文字列の書き方!!
class MergeIpAddressFiles:
    #ファイル数
    cnt = 0
    #コンストラクタ
    def __int__(self,cnt):
        #引数でファイル数を受け取る
        self.cnt = cnt

    def merge(self):
        #分割ファイルから重複を取り除き、ソートしたものをマージするSet
        mergeSet = set([])
        #マージしたSetをソートしなおしたSet
        sortedMergeSet = set([])
        #分割ファイルの数だけループする
        for no in range(0, self.cnt):
            #分割ファイル名を生成する
            sortFileName = "sortIpAddress{0:02d}.txt".format(no+1)
            #分割ファイルをオープンする
            sortIpAddressFile = open(sortFileName,"r")
            for setData in sortIpAddressFile:
                #1行ずつ読みながらSetに登録する
                mergeSet.add(setData)
            #分割ファイルをクローズする
            sortIpAddressFile.close()
        #すべての分割ファイルから読み込んだSetをソートする
        sortedMergeSet = sorted(mergeSet)
        #すべての分割ファイルから読み込んで、ソートしたものを１つのファイルに出力する
        mergeFile = open("resultMergeFile.txt","w")
        for setData in sortedMergeSet:
            mergeFile.write(setData)
        mergeFile.close()
