def knapsack_dp(W, wt, val, n): # W : 용량, wt : 무게, val : 가치, n: 물건의 개수
  A = [[0 for x in range(W+1)] for x in range(n+1)]

  for i in range(n+1):
    for w in range(W+1):
      if wt[i-1] > w:
        A[i][w] = A[i-1][w]
      else:
        valwith = val[i-1] + A[i-1][w-wt[i-1]]
        valwithout = A[i-1][w]
        A[i][w] = max(valwith, valwithout)
  return A[-1][-1]

val = [60, 100, 190, 120, 200, 150]
wt = [2, 5, 8, 4, 7, 6]
W = 18
n = len(val)
print(knapsack_dp(W, wt, val, n))