import networkx as nx
import matplotlib.pyplot as plt
with open("sortiePrim.txt", "r") as file:
    lines = file.readlines()
graph_edges = []

for line in lines:
    if line.startswith("Arbre couvrant minimal :") or line.startswith("Entrez le sommet de depart :") :
        continue
    parts = line.split()
    if len(parts) == 3 and not parts[0].startswith("Sommet"):
        try:
            graph_edges.append((parts[0], parts[1], int(parts[2])))
            print(f" {parts[0]} //// {parts[1]}  //// {parts[2]} ")
        except ValueError as e:
            print(f"Erreur lors de la conversion en entier : {e}")

print(f" {graph_edges} ")

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