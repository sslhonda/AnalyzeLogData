#coding: utf-8

import DivIpAddressFile
import SortIpAddressFile
import MergeIpAddressFiles

#TODO ドキュメンテーション文字列の書き方!!
def AnalyzeLogData():
    #検索対象文字列
    TARGET_STRING = "GET /?page_id="
    #ファイルを分割する際のカウンター
    fileCnt = 1
    #読み込んだ行数をカウント
    lineCnt = 0

    print("start analyze logdata")
    #読み込むログファイルを開く
    logfile = open("access_log","r")
    #１行ずつログファイルを読む
    for logline in logfile:
        #対象の文字列を探す。見つからなかったら読み飛ばす。
        if logline.find(TARGET_STRING)>=0:
            print("find target:{0}".format(logline))
            #対象の文字列が見つかったら
            #分割IPアドレスファイルの行数カウンタが0の場合
            if lineCnt==0:
                print("lineCnt:{0}, fileCnt:{1}".format(lineCnt,fileCnt))
                #分割IPアドレスファイルを開く
                divIpAddress = DivIpAddressFile.DivIpAddressFile(fileCnt)
                divIpAddress.openFile()
            lineCnt = lineCnt+1
            #分割IPアドレスファイルに書き込む文字列を切り出す。
            index = logline.find(" - - ")
            #切り出した文字列を分割IPアドレスファイルに書き込む。
            divIpAddress.writeFile(logline[0:index])
            #10,000行書き込んだら、分割IPアドレスファイルを
            if lineCnt>=10000:
                divIpAddress.closeFile()
                lineCnt = 0
                fileCnt = fileCnt + 1
            if fileCnt >= 100:
                #分割ファイルが99を超えたら中断
                break;
    #ログファイルが空だった場合にdivIpAddressは未定義になる
    divIpAddress.closeFile()
    #読み込んだログファイルを閉じる
    logfile.close()

    #分割ファイルを読み込んで、重複データ削除とソートを行う
    for cnt in range(0,fileCnt):
        print("fileNo:{0}".format(cnt))
        sortIpAddress = SortIpAddressFile.SortIpAddressFile(cnt+1)
        sortIpAddress.sortFile()

    #ソート済み分割ファイルをマージしたものを出力する
    mergeFile = MergeIpAddressFiles.MergeIpAddressFiles(fileCnt)
    mergeFile.merge()

    for cnt in range(0,fileCnt):
        deleteFileName = "divIpAddress{0:02d}.txt".format(cnt+1)
        os.remove(deleteFileName)
        deleteFileName = "sortIpAddress{0:02d}.txt".format(cnt+1)
        os.remove(deleteFileName)

    print("end analyze logdata")


AnalyzeLogData()
