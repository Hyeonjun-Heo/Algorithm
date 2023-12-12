def knapsack_fractional_greedy(obj, W):
  obj.sort(key = lambda o : o[2]/o[1], reverse = True) # 내림차순 정렬

  totalValue = 0
  for o in obj:
    if W <= 0: # 배낭에 용량이 다 찬 경우
      break
    if W - o[1] >= 0: # 물건 전체가 들어갈 수 있는 경우
      W -=[0]
      totalValue += o[2]
    else:
      fraction = W / o[1]
      totalValue += o[2] * fraction
      W = int(W - (o[1] * fraction))