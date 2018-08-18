# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 22:06:00 2018

@author: yuwan
"""

import sys

def grey(n,k):
    out = 0
    for i in range(n):
        out += ((not((k>>i)&1) == ((k >>(i+1)&1))) << i)
    return out

def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        n, k = [int(a) for a in sys.stdin.readline().split()]
        print(grey(n,k))
        
main()