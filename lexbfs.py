def lex_bfs(G):
  vertices = list(G.nodes())
  labels = {v: [] for v in vertices}
  unvisited = vertices.copy()

  ordem = []
  n = len(vertices)
  for i in range(n, 0, -1):
    v = max(unvisited, key=lambda x: labels[x])
    ordem.append(v)
    unvisited.remove(v)
    
    for u in G.neighbors(v):
      if u in unvisited:
        labels[u].insert(0, i)

  return ordem