import graph.graph as gt

if __name__ == '__main__':
    V = {'a', 'c', 'b', 'd', 'e'}
    E = {('b', 'c'), ('a', 'c'), ('a', 'b'), \
         ('a', 'd'), ('a', 'e'), ('b', 'd'), \
         ('c', 'd'), ('c', 'e'), ('b', 'e'), \
         ('d', 'e')}

    Vs = {'a', 'c', 'b', 'e'}
    Es = {('b', 'c'), ('a', 'b'), ('a', 'c'), ('a', 'e'), ('c', 'e'), ('b', 'e')}

    tv = gt.isinducedsubgraph(V, E, Vs, Es)
    print(tv)

    gt.drawgraph(E)
    gt.drawgraph(Es)