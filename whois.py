#http://kitaeng.hateblo.jp/entry/2016/03/03/223800
#上記サイトにあったコードを写経
#TODO これの意味することを理解する
#coding: utf-8

import sys
import ipaddress
from ipwhois import IPWhois

def swhois(ip):
    obj = IPWhois(ip)
    results = obj.lookup(get_referral=True)
    cc = results['asn_country_code']
    cidrs=[]
    for result_net in results['nets']:
        cidr = result_net['cidr'].split('/')[1]
        cidrs.append(int(cidr))
    ipwithcidr = str(ipaddress.IPv4Network(ip+'/'+str(max(cidrs)),False))
    return '{0} --> {1}{2}'.format(ip,ipwithcidr,cc)

#TODO これの意味することを理解する
if __name__ == '__main__':
    print(swhois(sys.argv[1]))
