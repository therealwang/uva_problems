# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:22:29 2018

@author: yuwan
"""

import sys

binary_tree_array = [1,1]

for i in range(2,1001):
    temp = 0
    for j in range(i):
        temp += binary_tree_array[j]* binary_tree_array[i-1-j]
    binary_tree_array.append(temp)
    
def main():
    while True:
        try:
            n = int(sys.stdin.readline())
        except:
            break
        print(binary_tree_array[n])

main()
    
