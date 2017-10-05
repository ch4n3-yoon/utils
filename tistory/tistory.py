#!/usr/bin/python
# coding: utf-8

import requests
import sys

__author__ = "ch4n3"

argv = sys.argv

if len(argv) != 5:
    print "[*] Usage :      {0} [tistory 계정] [검색] [google/naver] [횟수]".format(argv[0])
    print "[+] Example :    {0} chaneyoon \"sql injection\" google 100".format(argv[0])
    sys.exit(1)

tistoryAccount  = argv[1]
searchKeyword   = argv[2]
site            = argv[3]
cnt             = int(argv[4])


# Set tistory url
url = "http://{0}.tistory.com/".format(tistoryAccount)


# Set referer
if site == "naver":
    referer = 'https://search.naver.com/'
    referer += 'search.naver?sm=tab_hty.top&where=nexearch&query='+searchKeyword+'&oquery=%EC%9C%A4%EC%84%9D%EC%B0%AC+%ED%8C%AC%ED%81%B4%EB%9F%BD&tqi=TOKM4wpVuENsssSeZxhssssssQ4-326906'
else :
    site = "google"
    referer = 'https://www.google.co.kr/'
    referer += 'search?dcr=0&source=hp&q='+searchKeyword+'&oq='+searchKeyword
    referer += '&gs_l=psy-ab.3..35i39k1l2j0l8.63401.67062.0.67388.25.18.2.0.0.0.208.1968.0j8j3.12.0.dummy_maps_web_fallback...0...1.1j4.64.psy-ab..12.13.2037.6..0i10k1j0i131k1j0i3k1.188.2F7gO-l3NL8'


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
    'Referer': referer,
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}


print "="*30
print "[*] url  : {0}".format(url)
print "[*] Search Keyword   : {0}".format(searchKeyword)
print "[*] Referer site : {0}".format(site)
print "[*] Count    : {0}".format(cnt)
print "="*30

print "\n\nPress ctrl+c to exit\n\n"

try:
    for i in range(1, cnt+1):
        r = requests.get(url, headers=headers)
        print "조회수 +{0}".format(i)

except KeyboardInterrupt as e:
        print "종료!"
        sys.exit(0)
