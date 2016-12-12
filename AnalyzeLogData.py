#coding: utf-8

#TODO ドキュメンテーション文字列の書き方!!
def AnalyzeLogData():
    #検索対象文字列
    TARGET_STRING = "Get /?page_id="
    #ファイルを分割する際のカウンター
    fileCnt = 1
    #読み込んだ行数をカウント
    lineCnt = 0

    print("start analyze logdata")
    #読み込むログファイルを開く
    logfile = open("access_log","r")
    for logline in logfile:
        if logline.find(TARGET_STRING)>=0:
            if lineCnt==0:
                print("lineCnt:{0}, fileCnt:{1}".format(lineCnt,fileCnt))
                divIpAddress = DivIpAddressFile(fileCnt)
                divIpAddress.openFile()
            lineCnt = lineCnt+1
            index = logline.find(" - - ")
            divIpAddress.writeFile(logline[0:index])
            if lineCnt>=10000:
                divIpAddress.closeFile()
                lineCnt = 0
                fileCnt = fileCnt + 1
            if fileCnt >= 100:
                #分割ファイルが99を超えたら中断
                break;
    divIpAddress.closeFile()
    #ログファイルを閉じる
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

    print("end analyze logdata")


AnalyzeLogData()
