# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:19:28 2018

@author: yuwan
"""


import sys

INF = 1 << 32


from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(dict)
        
    ### Initializing ###
        
    def addEdge(self, inp, out, weight = None, digraph = False):
        self.vertices.update([inp, out])
        self.edges[inp][out] = weight
        
        if not digraph:
            self.edges[out][inp] = weight
            
    def alledges(self):
        edges = set()
        
        for i in self.edges:
            for j in self.edges[i]:
                edges.add((i,j,self.edges[i][j]))
                
        return edges
            
def floydwarshall(graph):
    #modified for longest path in dag
    out = {i: {o: 0 for o in graph.vertices} for i in graph.vertices}
    
    edges = graph.alledges()
    
    for i, j, d in edges:
        out[i][j] = d
        
        
    for k in graph.vertices:
        for i in graph.vertices:
            for j in graph.vertices:
                if out[i][j] < out[i][k] + out[k][j] and out[i][k] != 0 and out[k][j] != 0:
                    out[i][j] = out[i][k] + out[k][j]
        
    
    return out
        
                
        

def main():
    sys.stdin = open('test.txt','r')
    count = 0
    verts = int(sys.stdin.readline())
    while verts != 0:
        count += 1
        g = Graph()
        
        init = int(sys.stdin.readline())
        
        edge = [int(n) for n in sys.stdin.readline().split()]
        
        while edge != [0, 0]:
            g.addEdge(edge[0], edge[1], 1, True)
            edge = [int(n) for n in sys.stdin.readline().split()]
        
            
        out = floydwarshall(g)
        
        longest = end = 0
        for i in range(1, verts+1):
            if out[init][i] > longest:
                longest = out[init][i]
                end = i
        
        print 'Case {}: The longest path from {} has length {}, finishing at {}.\n'.format(
                count, init, longest, end
                )
        
        verts = int(sys.stdin.readline())
       
main()
            
        