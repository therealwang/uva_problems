# -*- coding: utf-8 -*-
"""
Created on Sat Sep 01 16:07:13 2018

@author: yuwan
"""

import sys

INF = 1 << 32

def longest_no_tree(l):
    dp = [0]*len(l)
    dp[0] = 0 if l[0] else 1
    for i in range(1, len(l)):
        if not l[i]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 0
    return max(dp)

def prefix_array(arr):
    for i in range(len(arr)):
        arr[i] = [sum(arr[i][:j+1]) for j in range(len(arr[i]))]
    return arr

def no_tree_rect(arr):
    arr = prefix_array(arr)
    cols = len(arr[0])
    temp = -INF
    for i in range(cols):
        for j in range(i, cols):
            if i == 0:
                newl = [arr[k][j] for k in range(len(arr))]
            else:
                newl = [arr[k][j] - arr[k][i-1] for k in range(len(arr))]
            temp = max(temp, longest_no_tree(newl) * (j-i+1))
    return temp

def main():
    m,n = [int(a) for a in sys.stdin.readline().split()]
    while m > 0:
        arr = []
        for i in range(m):
            arr.append([int(a) for a in sys.stdin.readline().split()])
        print(no_tree_rect(arr))
        m,n =[int(a) for a in sys.stdin.readline().split()]

main()