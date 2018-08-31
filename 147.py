# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 06:14:09 2018

@author: yuwan
"""

import sys

coins = [1,2,4,10,20,40,100,200,400,1000,2000]

dp =[[1]*6001 for i in coins]

for i in range(1,len(coins)):
    for j in range(1,6001):
        if j - coins[i] >= 0:
            dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
        else:
            dp[i][j] = dp[i-1][j]
            

def cc(num):
    return dp[len(coins)-1][num]
            

def main():
    curr = float(sys.stdin.readline().strip())
    while curr > 0:
        num = int(round(curr*100/5))
        print('{:6.2f}{:>17}'.format(curr,cc(num)))
        curr = float(sys.stdin.readline().strip())
        
main()