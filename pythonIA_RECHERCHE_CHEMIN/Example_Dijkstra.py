import networkx as nx
import matplotlib.pyplot as plt

#Créer un graphe non orienté avec des poids
G=nx.Graph()
G.add_weighted_edges_from([
    ('A','B',2),
    ('A','C',1),
    ('B','C',2),
    ('B','E',3),
    ('B','D',1),
    ('C','E',3),
    ('C','D',4),
    ('C','F',5),
    ('D','E',3),
    ('D','G',5),
    ('E','F',1),
    ('F','G',2)
    ])
#Positionner les noeuds
pos=nx.spring_layout(G,seed=42)

#Dessiner le graphe
nx.draw(G,pos,with_labels=True,font_weight='bold')

#Ajouter les labels des poids aux aretes
labels=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
#On affiche le graphe
plt.show()

#Recherche du plus court chemin
#Algorithme de DIJKSTRA
plus_court_chemin=nx.dijkstra_path(G, source='A', target='G')
#Afficher le plus court chemin
print("Le plus court chemin de A vers G est:", plus_court_chemin)

#Dessiner le graphe en mettant en evidence le plus court chemin
pos=nx.spring_layout(G,seed=42)
nx.draw(G,pos,with_labels=True,font_weight='bold')
nx.draw_networkx_edge_labels(G, pos,edge_labels=nx.get_edge_attributes(G,'weight'))
#Mise en evidence
nx.draw_networkx_edges(G,
                       pos,
                       edgelist=[(plus_court_chemin[i],
                                  plus_court_chemin[i+1]) for i in range(len(plus_court_chemin)-1)],
                       edge_color='r',
                       width=3)
plt.show()
