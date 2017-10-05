#!/usr/bin/python
# coding: utf-8

import requests
import sys


__author__ = "ch4n3"


tistoryAccount  = raw_input("[*] Tistory 계정 (*.tistory.com) : ")
searchKeyword   = raw_input("[*] 검색어 : ")
site            = raw_input("1. 구글 / 2. 네이버 : ")

if site == "2":
	referer = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+searchKeyword+'&oquery=%EC%9C%A4%EC%84%9D%EC%B0%AC+%ED%8C%AC%ED%81%B4%EB%9F%BD&tqi=TOKM4wpVuENsssSeZxhssssssQ4-326906'
else :
	referer = 'https://www.google.co.kr/search?dcr=0&source=hp&q='+searchKeyword+'&oq='+searchKeyword+'&gs_l=psy-ab.3..35i39k1l2j0l8.63401.67062.0.67388.25.18.2.0.0.0.208.1968.0j8j3.12.0.dummy_maps_web_fallback...0...1.1j4.64.psy-ab..12.13.2037.6..0i10k1j0i131k1j0i3k1.188.2F7gO-l3NL8'

url = 'http://{0}.tistory.com/'.format(tistoryAccount)


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
    'Referer': referer,
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}


i = 0

try:
    for i in range(1000):
        i += 1
        r = requests.get(url, headers=headers)
        print "조회수 +{0}".format(i)

except KeyboardInterrupt as e:
        print "종료!"
        sys.exit(0)
