def edit_distance_mem(S, T, m, n, mem):
  if m == 0:  # S가 공백이면, T의 모든 문자를 S에 삽입
    return n 
  if n == 0:  # T가 공백이면, S의 모든 문자를 삭제
    return m
  
  if mem[m-1][n-1] == None: # 아직 해결되지 않은 문제이면
    if S[m-1] == T[n-1]:
      mem[m-1][n-1] = edit_distance_mem(S, T, m-1, n-1, mem)

    else:
      mem[m-1][n-1] = 1 + \
        min(edit_distance_mem(S, T, m-1, n-1, mem), # 대체
            edit_distance_mem(S, T, m-1, n, mem), # 삽입
            edit_distance_mem(S, T, m, n-1, mem)) # 삭제
      
  return mem[m-1][n-1]

      