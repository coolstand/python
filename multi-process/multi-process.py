#!/usr/bin/env python2.7
#coding:utf-8
__author__ = 'junkizou'

import argparse
from datetime import *
import os
import sys
import re
import urllib2
import time
from multiprocessing import Pool

reload(sys)
sys.setdefaultencoding("utf-8")

MAX_NUM = 3

def Request():
    conn = urllib2.urlopen("http://www.baidu.com")
    if not conn:
        print "Request failed"
    else:
        print os.getpid(),conn.code

    if conn:
        conn.close()

if __name__ == '__main__':
    p = Pool(MAX_NUM)
    while 1:
        p.apply_async(Request)
        time.sleep(0.05)

    p.close()
    p.join()
    print "end"
