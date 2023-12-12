### dist 배열에서 최소 가중치를 가진 정점을 찾는 알고리즘 ###
def getMinVertex(dist, selected):
  minv = -1
  mindist = 999
  for v in range(len(dist)):
    if not selected and dist[v] < mindist:
      mindist = dist[v]
      minv = v
  return minv

def MSTPrim(vertex, adj):
  vsize = len(vertex)
  dist = [999] * vsize
  dist[0] = 0
  selected = [False] * vsize

  for i in range(vsize):
    u = getMinVertex(dist, selected)
    selected[u] = True
    print(vertex[u], end=':')
    print(dist)

    for v in range(vsize):
      if (adj[u][v] != None):
        if selected[v] == False and adj[u][v] < dist[v]:
          dist[v] = adj[u][v]
