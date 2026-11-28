import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.cm import ScalarMappable

from lexbfs import lex_bfs


# Cria um pequeno grafo cordal.
G = nx.Graph()
G.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E"),
])

# Executa o Lex-BFS.
ordem = lex_bfs(G)
print("Vertices:", list(G.nodes()))
print("Arestas:", list(G.edges()))
print("Ordem Lex-BFS:", ordem)

# Calcula as posições uma única vez para os dois gráficos ficarem iguais.
pos = nx.spring_layout(G, seed=42)

quantidade = len(ordem)

# Cria um degradê do amarelo bem claro até o vermelho-vinho.
cor_degrade = LinearSegmentedColormap.from_list(
    "amarelo_para_vinho",
    ["#fff9c4", "#800020"],
    N=max(2, quantidade)
)

# Associa cada vértice à sua posição na ordem Lex-BFS.
posicao_na_ordem = {vertice: i for i, vertice in enumerate(ordem)}

# Escolhe uma cor diferente para cada posição da ordem.
cores = [
    cor_degrade(posicao_na_ordem[v] / max(quantidade - 1, 1))
    for v in G.nodes()
]

# Monta os dois gráficos lado a lado.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 6))

# Gráfico 1: grafo original, com todos os vértices pretos.
nx.draw_networkx_edges(G, pos, ax=ax1, width=1.5)
nx.draw_networkx_nodes(
    G, pos, ax=ax1,
    node_color="black",
    node_size=900
)
nx.draw_networkx_labels(
    G, pos, ax=ax1,
    font_color="white",
    font_size=11
)
ax1.set_title("Grafo original")
ax1.axis("off")

# Gráfico 2: mesmas posições, com cores conforme a ordem Lex-BFS.
nx.draw_networkx_edges(G, pos, ax=ax2, width=1.5)
nx.draw_networkx_nodes(
    G, pos, ax=ax2,
    node_color=cores,
    node_size=900
)
nx.draw_networkx_labels(
    G, pos, ax=ax2,
    font_color="black",
    font_size=11
)
ax2.set_title("Grafo colorido pela ordem Lex-BFS")
ax2.axis("off")

# Barra de cores: amarelo = escolhido primeiro; vinho = escolhido por último.
if quantidade > 1:
    normalizacao = Normalize(vmin=1, vmax=quantidade)
    escala = ScalarMappable(norm=normalizacao, cmap=cor_degrade)
    escala.set_array([])
    fig.colorbar(
        escala,
        ax=ax2,
        fraction=0.046,
        pad=0.04,
        label="Posição na ordem Lex-BFS"
    )

plt.tight_layout()
plt.show()
