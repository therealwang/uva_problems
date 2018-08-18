# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 10:36:30 2018

@author: yuwan
"""

import sys

def main():
    maxheight = [0]* 10000
    while True:
        try:
            l, h, r = [int(a) for a in sys.stdin.readline().split()]
        except:
            break
        for i in range(l,r):
            maxheight[i] = max(maxheight[i], h)
    
    out = []
    currh = 0
    for i in range(10000):
        if maxheight[i] != currh:
            currh = maxheight[i]
            out.append('{} {}'.format(i,currh))
    
    print(' '.join(out))
    
main()