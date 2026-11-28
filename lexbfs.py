def lex_bfs(G):
    vertices = list(G.nodes())
    labels = {v: [] for v in vertices}
    unvisited = vertices.copy()
    ordem = []

    if not vertices:
        return ordem

    # A numeração cresce para que a escolha mais recente tenha prioridade.
    for i in range(1, len(vertices) + 1):
        v = max(unvisited, key=lambda x: labels[x])
        ordem.append(v)
        unvisited.remove(v)

        for u in G.neighbors(v):
            if u in unvisited:
                labels[u].insert(0, i)

    return ordem
