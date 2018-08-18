# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:58:41 2018

@author: yuwan
"""

import sys

def imp(l,n):
    out = [0]*(1<<n)
    for i in range(1<<n):
        for j in range(n):
            if i & (1<<j):
                mult = -1
            else:
                mult = 1
            out[i+mult*(1<<j)]+= l[i]
    
    tempmax = 0
    for i in range(1<<(n-1)):
        for j in range(n):
            rem = i % (1<<j)
            pref = i >> j
            tempmax = max(tempmax, out[rem + (1<<j) + (pref << (j+1))] +
                                       out[rem + (pref << (j+1))])

    return tempmax

def main():
    while True:
        try:
            n = int(sys.stdin.readline())
        except:
            break
        
        l = [0]* (1<<n)
        for i in range(1<<n):
            l[i] = int(sys.stdin.readline())
        print(imp(l,n))
        
main()