import graph.graph as gt

if __name__ == '__main__':
    m = 10
    n = 20
    [V, E] = gt.creategraph(m, n)
    print(V)
    print(E)
    gt.drawgraph(E)