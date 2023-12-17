import networkx as nx
import matplotlib.pyplot as plt
import re

# Lecture du fichier de sortie
with open("SortiePrim.txt", "r") as file:
    lines = file.readlines()

# Tableau pour stocker les arêtes avec leurs poids
graph_edges = []

# Expression régulière pour extraire les informations d'une ligne
regex = re.compile(r'\((\w+),(\w+)\) : (\d+)')

# Parse les arêtes du graphe
for line in lines:
    match = regex.match(line)
    if match:
        try:
            # Ajouter les arêtes au format (source, destination, poids)
            graph_edges.append((match.group(1), match.group(2), int(match.group(3))))
        except ValueError as e:
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
