# -*- coding: utf-8 -*-
"""
Created on Sat Sep 01 15:41:44 2018

@author: yuwan
"""

import sys
INF = 1 << 32

def kadane(l):
    dp = [0] * len(l)
    dp[0] = l[0]
    for i in range(1,len(l)):
        dp[i] = max(dp[i-1] + l[i], l[i])
    return max(dp)

def prefix_array(arr):
    for i in range(len(arr)):
        arr[i] = [sum(arr[i][:j+1]) for j in range(len(arr))]
    return arr


def kadane_2d(arr):
    arr=  prefix_array(arr)
    n = len(arr)
    temp = -INF
    for i in range(n):
        for j in range(i,n):
            if i == 0:
                newl = [arr[k][j] for k in range(n)]
            else:
                newl = [arr[k][j] - arr[k][i-1] for k in range(n)]
            temp = max(temp, kadane(newl))
    return temp


def main():
    a = int(sys.stdin.readline())
    l = []
    while True:
        try:
            nl = [int(k) for k in sys.stdin.readline().split()]
        except:
            break
        if len(nl) == 0:
            break
        l.append(nl)
    l = [i for sl in l for i in sl]
    arr = [l[i:i+a] for i in range(0, len(l), a)]
    print(kadane_2d(arr))
    
main()
        
    