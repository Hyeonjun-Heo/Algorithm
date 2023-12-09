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

while q: # while문을 통해서 갈 수 있는 도시의 정보들을 다 꺼냅니다. q가 비어있을 때 까지.
  cost, node = heapq.heappop(q)

  if dist[node] < cost :
    continue

  for i in graph[node]: # heapq를 통해 얻은 정보를 for문을 통해 graph에서 연결된 도시 정보를 끌어옵니다.
    newCost , newNode = 1, i
    

    distance = newCost + cost 
    if dist[newNode] > distance: # 연결된 도시의 거리정보를 계산한 다음 계속해서 거리정보 값들 중 가장 작은 값으로 갱신 해줍니다.
      dist[newNode] = distance
      heapq.heappush(q, (distance, newNode))
    
    else:
      continue
    
if dist.count(k) == 0:
  print(-1)
else:
  for j in range(1, n+1):
    if dist[j] == k:
      print(j)