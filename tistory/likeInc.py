#!/usr/bin/python
# coding: utf-8

import requests
import sys

argc = len( sys.argv )
if argc < 2:
    print "argv error"
    sys.exit(-1)

url = sys.argv[1]

"""
http://like.daum.net/item/tistory/2322212_284/like.json?callback=jQuery1110019596883896457307_1512839209392&token=Mt3FEgjpaWaMXo4XZU74coxi7fX/f0/Rju71BjgXP5/UD+vpObKq7UjGsPgzUgs7FlRedSwvwtLxJud7W4ILnwcml27CzvWsTjCHYZGdSbuhAzU4BErqbJvfRQOiYddnuu9d7uT+wIo=&sc=401,blogId_2322212&hc=126&created=20171210010040&fetchUrl=http://api.kakao.tistory.com/like/fetch?uid=2322212_284&pcUrl=http://chaneyoon.tistory.com/284&updateServiceCategory=true&scr=1
"""


