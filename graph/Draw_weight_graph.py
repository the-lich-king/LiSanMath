import graph.graph as gt

if __name__ == '__main__':
    m = 10
    n = 20
    [V, E] = gt.creategraph(m, n)
    [Vw, Ew] = gt.weightedgraph(V, E, 100)
    print(Ew)
    gt.drawweightgraph(Ew)