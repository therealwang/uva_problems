# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:32:35 2018

@author: yuwan
"""

import sys


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
            
            
def dijkstra(graph, start, end):
    if start not in graph.vertices or end not in graph.vertices:
        return 1e32
    
    unvisited = set()
    unvisited |= graph.vertices
    
    shortestpath = {v: 1e32 if v != start else 0 for v in graph.vertices}
    
    while unvisited:
        temp = {k: v for k, v in shortestpath.items() if k in unvisited}
        nextvert = min(temp, key = temp.get)
        if shortestpath[nextvert] == 1e32:
            return 1e32
        elif nextvert == end:
            return shortestpath[end]
        
        unvisited.remove(nextvert)
        
        for neighbor in graph.edges[nextvert]:
            templen = graph.edges[nextvert][neighbor] + shortestpath[nextvert]
            if templen < shortestpath[neighbor]:
                shortestpath[neighbor] = templen
                
                
        

def main():
    sys.stdin = open('test.txt','r')
    while True:
        
        try:
            num, targ = [int(n) for n in sys.stdin.readline().split()]
        except:
            break
        speeds = [int(n) for n in sys.stdin.readline().split()]
        floors = []
        for i in range(num):
            floors.append([int(n) for n in sys.stdin.readline().split()])
           
        g = Graph()
        for i in range(num):
            
            for inp, out in zip(floors[i],floors[i][1:]):
                g.addEdge((inp,i),(out,i), (out-inp) * speeds[i])
                
        for floor in range(100):
            for v1 in range(num):
                for v2 in range(num):
                    if (floor, v1) in g.vertices and (floor, v2) in g.vertices and v1 != v2:
                        g.addEdge((floor, v1),(floor,v2),60)
                        
               
        minimum = 1e32
        
        for v1 in range(num):
            for v2 in range(num):
                minimum = min(minimum,dijkstra(g, (0, v1), (targ, v2)))
                
        if minimum == 1e32:
            print 'IMPOSSIBLE'
        else:
            print minimum
       
main()
            
        