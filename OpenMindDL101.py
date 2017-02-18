# -*- coding: utf-8 -*-
import urllib
import os.path
import re

fileurl = "https://github.com/OpenMindClub/DeepLearningStartUp/raw/master/happiness_seg.txt"
filename = "happiness_seg.txt"
chinesepuncreg = ur"[\.\!\/_,$%^*(+\"\']+|[+——！，―。？、~@#￥%……&*（）：；《）《》“”()»〔〕-]+"
counters = {}

if not os.path.isfile(filename):
    urllib.urlretrieve(fileurl, filename)
f = open(filename)

for line in f.readlines():
    line = re.sub(chinesepuncreg, "", line.decode("utf8"))
    prev = ''
    #wordReg = re.compile("\w+", re.UNICODE)
    for word in line.split():
        if prev:
            pair = "%s %s" % (prev, word)
            counters[pair] = counters.get(pair, 0) + 1
        prev = word

for i in range(0,10):
    maxcount = -1
    maxpair = ""
    for pair, count in counters.items():
        if count > maxcount:
            maxcount = count
            maxpair = pair
    del counters[maxpair]
    print "%s %d" % (maxpair, maxcount)
