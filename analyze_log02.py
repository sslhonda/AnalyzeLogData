#coding: utf-8
import os
#クラス
#ipアドレス分割保存ファイル
class DivIpAddressFile:
    #
    no=0
    fileName =""
    #divIpAddressFile
    #コンストラクタ
    def __init__(self,no):
        self.no = no
        self.fileName = "divIpAddress{0}.txt".format('%02d' % self.no)

    def openFile(self):
        self.divIpAddressFile = open(self.fileName, "w")

    def closeFile(self):
        self.divIpAddressFile.close()

    def writeFile(self, str):
        self.divIpAddressFile.write(str)
        self.divIpAddressFile.write("\n")

class SortIpAddressFile:
    #
    no=0
    fileName=""
    sortFileName=""
    #コンストラクタ
    def __init__(self,no):
        self.no = no
        self.fileName = "divIpAddress{0}.txt".format('%02d' % self.no)
        self.sortFileName = "sortIpAddress{0}.txt".format('%02d' % self.no)

    def sortFile(self):
        ipAddressSet = set([])
        sortedIpAddressSet = set([])
        self.divIpAddressFile = open(self.fileName,"r")
        for readline in self.divIpAddressFile:
            ipAddressSet.add(readline)
        sortedIpAddressSet = sorted(ipAddressSet)
        self.divIpAddressFile.close()
        print("fileName:{0},{1}",self.fileName,len(ipAddressSet))
        self.sortIpAddressFile = open(self.sortFileName,"w")
        for setData in sortedIpAddressSet:
            self.sortIpAddressFile.write(setData)
        self.sortIpAddressFile.close()
        #os.remove(self.fileName)

class MergeIpAddressFiles:
    #ファイル数
    cnt=0
    #コンストラクタ
    def __init__(self,cnt):
        self.cnt = cnt

    def merge(self):
        mergeSet = set([])
        sortedMergeSet = set([])
        for no in range(0,self.cnt):
            sortFileName = "sortIpAddress{0:02d}.txt".format(no+1)
            sortIpAddressFile = open(sortFileName,"r")
            for setData in sortIpAddressFile:
                mergeSet.add(setData)
            sortIpAddressFile.close()
            #ソートファイル削除
            #os.remove(sortFileName)
        sortedMergeSet = sorted(mergeSet)
        mergeFile = open("resultMergeFile.txt","w")
        for setData in sortedMergeSet:
            mergeFile.write(setData)
        mergeFile.close()

def analyze_logdata():
    #対象文字列
    TARGET_STRING="GET /diary/"
    fileCnt=1
    lineCnt=0
    print("start analyze_logdata")
    #logファイルを開く
    logfile = open("access_log","r")
    for logline in logfile:
        if logline.find(TARGET_STRING)>=0:
            if lineCnt==0:
                print("linCnt:{0}, fileCnt:{1}".format(lineCnt,fileCnt))
                divIpAddress = DivIpAddressFile(fileCnt)
                divIpAddress.openFile()
            lineCnt=lineCnt+1
            index = logline.find(" - - ")
            divIpAddress.writeFile(logline[0:index])
            #print(logline[1:index])
            if lineCnt>=10000:
                divIpAddress.closeFile()
                lineCnt=0
                fileCnt = fileCnt+1
            if fileCnt>=100:
                #分割ファイルが99を超えたら中断
                break;
    divIpAddress.closeFile()
    #logファイルを閉じる
    logfile.close()

    #分割ファイルを読み込んで、重複データ削除とソートを行う
    for cnt in range(0,fileCnt):
        print("fileNo:{0}".format(cnt))
        sortIpAddress = SortIpAddressFile(cnt+1)
        sortIpAddress.sortFile()

    #ソート済み分割ファイルをマージしたものを出力する
    mergeFile = MergeIpAddressFiles(fileCnt)
    mergeFile.merge()

    for cnt in range(0,fileCnt):
        deleteFileName = "divIpAddress{0:02d}.txt".format(cnt+1)
        os.remove(deleteFileName)
        deleteFileName = "sortIpAddress{0:02d}.txt".format(cnt+1)
        os.remove(deleteFileName)


    print("end analyze_logdata")

analyze_logdata()
