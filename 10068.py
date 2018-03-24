# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:56:27 2018

@author: yuwan
"""


from collections import defaultdict, deque
import sys
INF = 1 << 32

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(dict)
        
    ### Initializing ###
        
    def addEdge(self, inp, out, weight = 1, digraph = False):
        self.vertices.update([inp, out])
        self.edges[inp][out] = weight
        
        if not digraph:
            self.edges[out][inp] = weight
            
    
def generateGraph(r, c):
    sys.stdin = open('test.txt','r')
    g = Graph()
    treasures =[]
    for i in range(r):
        verts = [v for v in sys.stdin.readline().strip()]
        for v, j in zip(verts, range(c)):
            if v != '#':
                g.vertices.add((i,j))
            if v == '*':
                treasures.append((i,j))
            if v == 'S':
                init = (i,j)
            if v == 'T':
                out = (i,j)
                
    for i in range(r-1):
        for j in range(c-1):
            if (i,j) in g.vertices and (i,j+1) in g.vertices:
                g.addEdge((i,j),(i,j+1))
            if (i,j) in g.vertices and (i+1,j) in g.vertices:
                g.addEdge((i,j),(i+1,j))
                
                
    return g, treasures, init, out


def 