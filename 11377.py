# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:27:05 2018

@author: yuwan
"""

import sys

INF = 1 << 32


from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(dict)
        self.hasairports = set()
        
    ### Initializing ###
        
    def addEdge(self, inp, out, weight = None, digraph = False):
        self.vertices.update([inp, out])
        self.edges[inp][out] = weight
        
        if not digraph:
            self.edges[out][inp] = weight
            
            
def dijkstra(graph, start, end):
    if start not in graph.vertices or end not in graph.vertices:
        return INF
    if start == end:
        return 0
    
    unvisited = set()
    unvisited |= graph.vertices
    
    shortestpath = {v: INF if v != start else 0 for v in graph.vertices}
    
    while unvisited:
        temp = {k: v for k, v in shortestpath.items() if k in unvisited}
        nextvert = min(temp, key = temp.get)
        if shortestpath[nextvert] == INF:
            return -1
        elif nextvert == end:
            shortestpath[end] += not start in graph.hasairports
            return shortestpath[end]
        
        unvisited.remove(nextvert)
        
        for neighbor in graph.edges[nextvert]:
            templen = graph.edges[nextvert][neighbor] + shortestpath[nextvert]
            if templen < shortestpath[neighbor]:
                shortestpath[neighbor] = templen
                
 
               
        

def main():
    #sys.stdin = open('test.txt','r')
    cases = int(sys.stdin.readline())
    for case in range(1, cases+1):
        N, M, K = [int(a) for  a in sys.stdin.readline().split()]
        g = Graph()
        g.hasairports = set([int(a) for a in sys.stdin.readline().split()])
        for m in range(M):
            i, o = [int(a) for a in sys.stdin.readline().split()]
            g.addEdge(o, i, not i in g.hasairports, True)
            g.addEdge(i, o, not o in g.hasairports, True)
        Q = int(sys.stdin.readline())
        print('Case {}:'.format(case))
        for q in range(Q):
            di, do = [int(a) for a in sys.stdin.readline().split()]
            print(dijkstra(g,di, do))
        print('')
        #sys.stdin.readline()
            
            
main()        