#!/usr/bin/env python2.7
#coding:utf-8
__author__ = 'junkizou'

import argparse
#import datetime, time
from datetime import *
import os
import sys
import re
import threading
import urllib2

reload(sys)
sys.setdefaultencoding("utf-8")

Link = "http://www.baidu.com"
Headers = {'Content-Type':'text/html; charset=utf-8'}

MAX_NUM = 3

def Request(num):
    conn = urllib2.urlopen(Link)
    if not conn:
        print "Request failed"
    else:
        print i, conn.code

    if conn:
        conn.close()

if __name__=='__main__':
    threads = []

    for i in range(MAX_NUM):
        t = threading.Thread(target=Request(i))
        threads.append(t)

    for i in range(MAX_NUM):
        #threads[i].setDaemon(True)#//守护线程，其作用与join相反，当主线程执行到此处时，无须等待子线程的返回，继续执行，当父线程结束时，此守护线程（子线程）也一起结束。
        threads[i].start()

    for i in range(MAX_NUM):
        threads[i].join()#//join,用于主线程阻塞等待子线程执行结束。

    print"end"
