import networkx as nx
import matplotlib.pyplot as plt

with open("SortiePrim.txt", "r") as file:
    lines = file.readlines()

# Tableau pour stocker les arêtes avec leurs poids
graph_edges = []

for line in lines:
    parts = line.split()
    try:
        #ON VA AJOUTER LES ELEMENT DE PARTS DANS LE GRAPH_EDGES
        graph_edges.append((parts[0], parts[1], int(parts[2])))
    except ValueError as e:
        #SINON UNE EXCPTION SERA LANCEE
        print(f"Erreur lors de la conversion en entier : {e}")

# Créer le graphe à l'aide de NetworkX
G = nx.Graph()
G.add_weighted_edges_from(graph_edges)

# Dessiner le graphe
pos = nx.spring_layout(G)  
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, edge_color='gray', width=1, alpha=0.7, arrowsize=10)

# Ajouter les poids des arêtes au-dessus de celles-ci
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Afficher le graphe
plt.show()
