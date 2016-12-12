#coding: utf-8

#TODO ドキュメンテーション文字列の書き方!!
class SortIpAddressFile:
    #分割ファイルNo(01～99,00もいいよ)
    no=0
    fileName=""
    sortFileName=""

    #コンストラクタ
    def __init__(self,no):
        #コンストラクタ引数のNoを受け取る
        self.no = no
        #受け取ったNoから分割ファイル名を生成する。
        self.fileName = "divIpAddress{0}.txt".format('%02d' % self.no)
        #受け取ったNoからソート済みIPアドレスファイル名を生成する。
        self.sortFileName = "sortIpAddress{0}.txt".format('%02d' % self.no)

    def sortFile(self):
        #ipアドレスを重複なく管理する入れ物
        ipAddressSet = set([])
        #ソート済みのipアドレスを重複なく管理する入れ物
        sortedIpAddressSet = set([])
        #分割ファイルをオープン
        self.divIpAddressFile = opne(sefl.fileName,"r")
        #分割ファイルから１行ずつ読み込む
        for readline in self.divIpAddressFile:
            #setに登録することで、IPアドレスの重複を省く
            ipAddressSet.add(readline)
        #setをソートする
        sortedIpAddressSet = sorted(ipAddressSet)
        #分割ファイルをクローズする
        self.divIpAddressFile.close()
        print("fileName:{0},{1}", self.fileName, len(ipAddressSet))
        #ソート済みIPアドレスファイルを開く
        self.sortIpAddressFile = open(self.sortFileName,"w")
        #重複なしソート済みをIPアドレスをファイルに出力する
        for setData in sortedIpAddressSet:
            self.sortIpAddressFile.write(setData)
        #ソート済みIPアドレスファイルを閉じる
        self.sortIpAddressFile.close()
        
