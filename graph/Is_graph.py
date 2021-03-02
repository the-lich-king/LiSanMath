import graph.graph as gt

if __name__ == '__main__':
    V = {1, 2, 3, 4, 5, 6}
    E = {(1, 2), (2, 3), (4, 5), (5, 6), (1, 4), (2, 5), (3, 6), \
         (1, 5), (2, 6), (3, 4)}
    
    tv = gt.isgraph(V, E)
    print(tv)
    gt.drawgraph(E)