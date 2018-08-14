# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 20:43:07 2018

@author: yuwan
"""

import sys
from collections import defaultdict
from math import sqrt

def LCC(edges, rings):
    n = rings
    s = set(range(n))
    max_set = 0
    while s:
        vert = s.pop()
        neighbors = set([v for v in edges[vert] if v in s])
        temp = 1
        while neighbors:
            next_vert = neighbors.pop()
            s.remove(next_vert)
            temp += 1
            neighbors.update([v for v in edges[next_vert] if v in s])
        max_set = max(max_set, temp)
    return max_set
            

def main():
    rings = int(sys.stdin.readline())
    while rings != -1:
        verts = {}
        edges = defaultdict(list)
        for ring in range(rings):
            nl = sys.stdin.readline().split()
            x, y, r = [float(a) for a in nl]
            verts[ring] = (x,y,r)
            for other_ring in range(ring):
                o = verts[other_ring]
                minr = min(r, o[2])
                dist = sqrt((x-o[0])**2+(y-o[1])**2)
                if dist <= r + o[2] and dist + minr >= max(r, o[2]):
                    edges[ring].append(other_ring)
                    edges[other_ring].append(ring)
        largest = LCC(edges, rings)
        print('The largest component contains {} ring{}.'.format(largest,
              's' if largest != 1 else ''))
        rings = int(sys.stdin.readline())
        
main()
                    