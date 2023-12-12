import copy
def Shortest_path_floyd(vertex, W):
  vsize = len(vertex) # 정점의 개수
  D = copy.deepcopy(W) # 깊은 복사

  for k in range(vsize): # 정점 k를 추가할 때
    for i in range(vsize):
      for j in range(vsize): # 모든 D[i][j] 갱신
        if (D[i][k] + D[k][j] < D[i][j]):
          D[i][j] = D[i][k] + D[k][j]
  print(D)