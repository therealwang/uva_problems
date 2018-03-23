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
    out = {i: {o: -INF for o in graph.vertices} for i in graph.vertices}
    
    for i in graph.vertices:
        out[i][i] = 0
    
    edges = graph.alledges()
    
    for i, j, d in edges:
        out[i][j] = d
        
        
    for k in graph.vertices:
        for i in graph.vertices:
            for j in graph.vertices:
                    out[i][j] = max(out[i][j],out[i][k] + out[k][j])
        
    
    return out

def bellmanford(g, source):
    #using bellman ford
    dist = defaultdict(lambda:-INF)
    pred = defaultdict(lambda:None)
    
    dist[source] = 0
    
    edges = g.alledges()
    
    for i in range(len(g.vertices)):
        for i, o, d in edges:
            if dist[i] + d > dist[o]:
                dist[o] = dist[i] + d
                pred[o] = i
            
    return dist
        
                
        

def main():
    #sys.stdin = open('test.txt','r')
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
        
            
        out = bellmanford(g, init)
        
        longest = end = 0
        for i in range(1, verts+1):
            if out[i] > longest:
                longest = out[i]
                end = i
        
        print( 'Case {}: The longest path from {} has length {}, finishing at {}.\n'.format(
                count, init, longest, end
                ))
        
        verts = int(sys.stdin.readline())
       
main()
            
        