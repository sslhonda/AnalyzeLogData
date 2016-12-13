#coding: utf-8

import ipaddress
from ipwhois import IPWhois

#TODO ドキュメンテーション文字列の書き方!!
class MergeIpAddressFiles:
    #ファイル数
    cnt = 0
    #コンストラクタ
    def __init__(self,cnt):
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
            for ipAddress in sortIpAddressFile:
                ipAddress = ipAddress.replace("\n","")
                ipAddress = ipAddress.replace("\r","")
                #読み込んだIPアドレスにwhois
                obj = IPWhois(ipAddress)
                #何しているのかよくわからない
                results = obj.lookup_whois(get_referral=True)
                cc = results["asn_country_code"]
                cidrs=[]
                for result_net in results["nets"]:
                    cidr = result_net["cidr"].split("/")[1]
                    cidrs.append(int(cidr))
                ipwithcidr = str(ipaddress.IPv4Network(ipAddress+"/"+str(max(cidrs)),False))
                retstr = "{0}-->{1}{2}".format(ipAddress,ipwithcidr,cc)
                print(retstr)
                #1行ずつ読みながらSetに登録する
                mergeSet.add(retstr)
            #分割ファイルをクローズする
            sortIpAddressFile.close()
        #すべての分割ファイルから読み込んだSetをソートする
        sortedMergeSet = sorted(mergeSet)
        #すべての分割ファイルから読み込んで、ソートしたものを１つのファイルに出力する
        mergeFile = open("resultMergeFile.txt","w")
        for setData in sortedMergeSet:
            mergeFile.write(setData)
        mergeFile.close()
