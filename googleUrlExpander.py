#!/usr/bin/python
# coding: utf-8

import requests
import sys

argc = len(sys.argv)

if argc < 2:
    print "[*] Usage : {0} [Google short URL]".format(sys.argv[0])
    sys.exit(-1)

# url = raw_input("Input Google short URL : ")
# url = "https://goo.gl/Hs6bUv"
url = sys.argv[1]


r = requests.get(url)
print "\n[*] The REAL url : {0}\n".format(r.url)