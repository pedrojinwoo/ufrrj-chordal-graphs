import networkx as nx
from lexbfs import lex_bfs

G = nx.Graph()

G.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E")
])

print("Vertices:", list(G.nodes()))
print("Arestas:", list(G.edges()))

print("Ordem Lex-BFS:", lex_bfs(G))