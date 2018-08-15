# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:29:40 2018

@author: yuwan
"""

import sys


class queueDict(dict):
    def __init__(self, n, *arg, **kw):
        super(queueDict, self).__init__(*arg, **kw)
        self.n = n
        
    def __missing__(self,key):
        value = self[key] = [(key-1)%self.n, (key+1)%self.n]
        return value

def main():
    i = 1
    while True:
        n, c = [int(a) for a in sys.stdin.readline().split()]
        if n == 0:
            break
        
        print('Case {}:'.format(i))
        
        d = queueDict(n)
        np = 0
        for _ in range(c):
            command = sys.stdin.readline().strip()
            if command == 'N':
                print(np+1)
                np = d[np][1]
            else:
                override_np = int(command.split()[1]) - 1
                if np == override_np:
                    pass
                else:
                    prev_n, next_n = d[override_np]
                    d[prev_n][1] = next_n
                    d[next_n][0] = prev_n
                    d[d[np][0]][1] = override_np
                    d[override_np][0] = d[np][0]
                    d[override_np][1] = np
                    d[np][0] = override_np
                    np = override_np
            
            
        i+=1

main()