#!/usr/bin/env python2.7
#coding:utf-8
__author__ = 'junkizou'

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def Request(i):
    conn = urllib2.urlopen("http://www.baidu.com")
    if not conn:
        print "Request failed"
    else:
        print i,conn.code

    if conn:
        conn.close()

if __name__ == '__main__':

    routine_list = []
    for i in range(10):
        routine_list.append(gevent.spawn(Request,i))

    gevent.joinall(routine_list)    

    print "end"
    
