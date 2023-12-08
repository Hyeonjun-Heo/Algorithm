import sys
import heapq

n,m,k,x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] *(n+1) for _ in range(n+1)]

for _ in range(m):
  node1, node2 = map(int, sys.stdin.readline().rstrip().split())

  graph[node1].append(node2) # node1 이웃 목록에 node2를 추가합니다.

q = [(0,x)] # heapq 에는 (거리, 도시) 값이 들어갑니다. 초기 값은 (0, 시작 도시)로 설정합니다.

dist = [1e9] * (n+1) # dist는 거리를 계산하여 담을 배열입니다.
dist[x] = 0 # 시작점 ~ 시작점의 거리는 0으로 초기화해줍니다.

while q:
  cost, node = heapq.heappop(q)

  if dist[node] < cost :
    continue