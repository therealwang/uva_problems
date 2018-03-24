# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 17:12:58 2018

@author: yuwan
"""

import sys
INF = 1 << 32

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(dict)
        self.validjugs = set()
        
    ### Initializing ###
        
    def addEdge(self, inp, out, weight = None, digraph = False):
        self.vertices.update([inp, out])
        self.edges[inp][out] = weight
        
        if not digraph:
            self.edges[out][inp] = weight
            
            
def dijkstra(graph, start, endverts):
    endverts = set(endverts)
    
    unvisited = set()
    unvisited |= graph.vertices
    
    shortestpath = {v: INF if v != start else 0 for v in graph.vertices}
    mindist = INF
    
    while unvisited:
        temp = {k: v for k, v in shortestpath.items() if k in unvisited}
        nextvert = min(temp, key = temp.get)
        if shortestpath[nextvert] == INF:
            return INF
        elif nextvert in endverts:
            endverts.remove(nextvert)
            mindist = min(shortestpath[nextvert], mindist)
            if not endverts:
                return mindist
        
        unvisited.remove(nextvert)
        
        for neighbor in graph.edges[nextvert]:
            templen = graph.edges[nextvert][neighbor] + shortestpath[nextvert]
            if templen < shortestpath[neighbor]:
                shortestpath[neighbor] = templen


def generateGraph(j1, j2, j3):
    alljugs = [j1, j2, j3]
    g = Graph()
    q = deque([(0,0,j3)])
    
    while q:
        nextvert = q.pop()
        for i in range(3):
            for j in range(3):
                tempneighbor = list(nextvert)
                if nextvert[j] < alljugs[j] and nextvert[i] > 0:
                    weight = min(nextvert[i],alljugs[j]-nextvert[j])
                    tempneighbor[i] -= weight
                    tempneighbor[j] += weight
                    g.validjugs.update(tempneighbor)
                    tempneighbor = tuple(tempneighbor)
                    if tempneighbor not in g.vertices:
                        q.append(tempneighbor)
                    g.addEdge(nextvert, tempneighbor, weight, True)
    
    return g
    
def main():
    cases = int(sys.stdin.readline())
    for i in range(cases):
        j1, j2, j3, targ = [int(a) for a in sys.stdin.readline().split()]
        g = generateGraph(j1, j2, j3)
        targ = max([a for a in g.validjugs if a <= targ])
        validverts = [vert for vert in g.vertices if targ in vert]
        
        mindist = dijkstra(g, (0,0,j3), validverts)
            
        print('{} {}'.format(mindist, targ))
        
main()
            