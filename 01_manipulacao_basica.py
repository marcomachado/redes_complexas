# %%
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# %%
G = nx.Graph()

# %%
G.add_node('Node1')
G.add_node('Node2')
G.add_node('Node3')
G.add_node('Node4')
G.add_node('Node5')
G.add_node('Node6')

# %%
G.add_edge('Node1', 'Node2')
G.add_edge('Node2', 'Node3')
G.add_edge('Node1', 'Node3')
G.add_edge('Node2', 'Node4')
G.add_edge('Node3', 'Node5')
G.add_edge('Node5', 'Node6')

# %%
pos = nx.spring_layout(G)
nx.draw(G, with_labels = True, node_size=500, font_size=16, pos = pos)
plt.show(True)

# %%
G.remove_edge('Node1','Node2')
G.remove_edge('Node1', 'Node3')

# %%
nx.draw(G, with_labels = True, node_size=500, font_size=16, pos = pos)
plt.show(True)
# %%
G.add_node('Node1')


# %%
G.add_node('Node3')
nx.draw(G, with_labels = True, node_size=500, font_size=16, pos = pos)
plt.show(True)

# %%
Gw = nx.Graph()
Gw.add_edge('a', 'b', weight=0.1)
Gw.add_edge('a', 'c', weight=0.5)
Gw.add_edge('b', 'c', weight=0.3)
Gw.add_edge('a', 'd', weight=0.9)

# %%
import matplotlib.pyplot as plt
labels = Gw.nodes()
posw = nx.spring_layout(Gw)
nx.draw(Gw, with_labels=True, node_color = 'r', node_size=500,font_size=16, 
        pos=posw, width=6)
nx.draw_networkx_edge_labels(Gw, posw)
plt.savefig('graphw.pdf')
plt.show(True)

# %%
Gw.add_edge(1, 2, weight=4.0)
Gw.add_edge(1, 'a')

# %%
labels = Gw.nodes()
posw = nx.circular_layout(Gw)
nx.draw(Gw, with_labels=True, node_color = 'r', edge_color='b',
        node_size=500,font_size=16, 
        pos=posw, width=6)
nx.draw_networkx_edge_labels(Gw, posw)
plt.savefig('graphw.pdf')
plt.show(True)

# Matriz de adjacências

# %%
A = [
        [0,1,0,0,0],
        [1,0,1,1,1],
        [0,1,0,1,0],
        [0,1,0,0,0],
        [0,1,0,0,0]
]
G = nx.from_numpy_array(np.array(A))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_size=500,font_size=16, 
        pos=pos)
plt.show()

# %%
G.clear()
edgeList = [(0,1),(1,2),(2,3),(3,1),(4,1)]
G = nx.Graph(edgeList)
nx.draw(G, with_labels=True, node_size=500,font_size=16, 
        pos=pos)
plt.show()

# Arestas dirigidas
# %%
G.clear()
edgeList = [(0,1),(1,2),(2,3),(3,1),(4,1)]
G = nx.DiGraph(edgeList)
nx.draw(G, with_labels=True, node_size=500,font_size=16, 
        pos=pos)
plt.show()
# %%
G.clear()
G = nx.Graph()

G.add_node('Node1')
G.add_node('Node2')
G.add_node('Node3')
G.add_node('Node4')
G.add_node('Node5')
G.add_node('Node6')

G.add_edge('Node1', 'Node2', time='10pm')
G.add_edge('Node2', 'Node3')
G.add_edge('Node1', 'Node3')
G.add_edge('Node2', 'Node4')
G.add_edge('Node3', 'Node5')
G.add_edge('Node5', 'Node6')

G.add_node('Node7', time='5pm')
G.add_edge('Node6', 'Node7')

pos = nx.spring_layout(G)
nx.draw(G, with_labels = True, node_size=500, font_size=16, pos = pos)
plt.show(True)
# %%
print(G.nodes['Node7'])
print(G.nodes['Node6'])
# %%
print(G.edges['Node1', 'Node2'])
# %%
for node in G.nodes():
        print('Node: ',node)
# %%
G = nx.convert_node_labels_to_integers(G, first_label=0)
for node in G.nodes():
        print('Node: ',node)
# %%
for edge in G.edges():
        print(edge)
# %%
for edge in G.edges(data=True):
        print(edge)
# %%
for edge in G.edges():
        G[edge[0]][edge[1]]['weight']=1.5

for edge in G.edges(data=True):
        print(edge)

# exemplo usando rede de escola de karate

# %%
G.clear()
G = nx.karate_club_graph()
subset = [0,1,2,3,4,5, 'node test']

pos = nx.spring_layout(G)

k = G.subgraph(subset)

plt.figure(figsize=(10,6))

nx.draw_networkx(G, pos=pos, node_color='g')
nx.draw_networkx(k, pos=pos, node_color='r')
plt.show()

# união de grafos

# %%

G1 = nx.Graph([(0,1), (1,2), (2,0)])
nx.draw(G1, with_labels = True, node_size=500, font_size=16)
plt.show()

G2 = nx.Graph([(0,1), (1,2), (2,3), (3,4), (2,4)])
nx.draw(G2, with_labels = True, node_size=500, font_size=16)
plt.show()

G3 = nx.disjoint_union(G1, G2)
nx.draw(G3, with_labels = True, node_size=500, font_size=16)
plt.show()

G4 = nx.compose(G1, G2)
nx.draw(G4, with_labels = True, node_size=500, font_size=16)
plt.show()

# converter grafo direcionado em não-direcionado
# G.to_undirected()

#convert grafo não-direcionado em direcionado (dígrafo)
# G.to_directed()

# Componentes

# %%
G = nx.Graph([
        (0,1), (1,2),
        (2,3), (3,4),
        (2,4), (5,6),
        (6,7), (8,9),
])
pos = nx.fruchterman_reingold_layout(G)
nx.draw(G, with_labels=True, node_size=500, font_size=16, pos=pos)
plt.show()
# %%
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
print(Gcc)

#Maior componente
# %%
print(Gcc[0])
G0 = G.subgraph(Gcc[0])
nx.draw(G0, with_labels=True)

# remover arestas e/ou vértices
# acessar vizinhos: G.neighbors (colorir vizinhos)
# vizinhos: personagens de livros que interagem com outro
