#coding: utf-8

#TODO ドキュメンテーション文字列の書き方!!
class DivIpAddressFile:
    #分割ファイルNo(01～99,00もいいよ)
    no=0
    #分割ファイル名定数
    DivFileName="divIpAddress{0}.txt"
    #分割ファイル名
    fileName=""
    #コンストラクタ
    def __init__(self, no):
        #コンストラクタ引数のNoを受け取る
        self.no = no
        #受け取ったNoから分割ファイル名を生成する。
        self.fileName = self.DivFileName.format('%02d' % self.no)

    #分割ファイルをオープンする
    def openFile(self):
        #書き込み可能ファイルとして、分割ファイルを開く
        self.divIpAddressFile = open(self.fileName, "w")
        #TODO: 例外処理必要では

    #分割ファイルをクローズする
    def closeFile(self):
        #分割ファイルを閉じる
        self.divIpAddressFile.close()

    #分割ファイルに書き込む
    def writeFile(self, str):
        #分割ファイルに引数の文字列を書き込む
        self.divIpAddressFile.write(str)
        #分割ファイルに行末のリターンコードを書き込む
        self.divIpAddressFile.write("\n")
