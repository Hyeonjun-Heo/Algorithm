def lcs_dp (X, Y):
  m = len(X)
  n = len(y)
  L = [[None]*(n+1) for _ in range(m+1)] # 테이블 생성

  for i in range(m+1):
    for j in range(n+1):
      if i == 0 or j == 0: # base case : 하나의 길이라도 0이면 
        L[i][j] = 0 # LCS = 0
      elif X[i-1] == Y[i-1]: # 마지막 글자가 같으면
        L[i][j] = L[i-1][j-1] + 1
      else: # 마지막 글자가 다르면
        L[i][j] = max(L[i-1][j], L[i][j-1])

  return L[m][n]

### LCS 테이블에서 LCS를 추적하는 알고리즘 ###

def lcs_dp_traceback(X, Y, L):
  lcs = ""
  i = len(X)
  j = len(Y)
  while i > 0 and j > 0:
    v = L[i][j]
    if v > L[i][j] and v > L[i-1][j] and v > L[i-1][j-1]:
      i -= 1
      j -= 1
      lcs = X[i] + lcs
    elif v == L[i][j] and v > L[i-1][j]:
      