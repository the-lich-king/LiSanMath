import random
import networkx as nx
import matplotlib.pyplot as plt

def Cartesianproduct(X, Y):     #生成边
    XY = set({})
    for x in X:
        for y in Y:
            XY.add((x, y))
    return XY

def creategraph(m, n):          #随机生成图
    global V, XY
    V = range(m)
    XY = Cartesianproduct(V, V)
    E = random.sample(XY, n)
    return [V, E]

def Cartesianproductweight(X, Y):   #生成有向边
    XY = set({})
    for x in X:
        for y in Y:
            weight  = random.randint(1, 100)
            XY.add((x, y, weight))
    return XY

def weightedgraph(V0, E0, W0):  #生成权图
    V = V0
    E = set({})
    for (u, v) in E0:
        w = random.randint(1, W0)
        E = E | {(u, v, w)}
    return [V, E]


def drawgraph(E):               #画图
    G = nx.Graph()
    G.add_edges_from(E)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='w')
    plt.show()
    return

def drawweightgraph(E):         #画权图
    G = nx.Graph()
    G.add_weighted_edges_from(E)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='w')
    plt.show()
    return

def drawdigraph(E):             #画有向图
    G = nx.DiGraph()
    G.add_edges_from(E)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='w')
    plt.show()
    return

def isgraph(V, E):              #判断是否为图
    tv = True
    for (u, v) in E:
        tv = tv and (u in V) and (v in V)
    return tv

def issubgraph(V, E, Vs, Es):   #判断是否为子图
    tv = (Vs <= V) and (Es <= E)
    return tv

def ispropersubgraph(V, E, Vs, Es): #判断是否为真子图
    tv = ((Vs <= V) and (Es <= E)) and ((Vs < V) or (Es < E))
    return tv

def isspanningsubgraph(V, E, Vs, Es):   #判断是否为生成子图
    tv = ((Vs <= V) and (Es <= E)) and ((Vs == V) and (Es <= E))
    return tv

def isinducedsubgraph(V, E, Vs, Es):    #判断是否为导出子图
    tv = (Vs <= V) and (Es <= E)
    for (u, v) in E:
        tv = tv and ((not((u in Vs) and (v in Vs))) or ((u, v) in Es))
    return tv