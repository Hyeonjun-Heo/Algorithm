# 첫 번째로 양의 정수 n,m을 입력 받고 두번째로 n개의 숫자를 입력 받는다. 3<= n <=100, 10<= m <= 300,000
# N개의 숫자 중 3개의 숫자를 골라서 m을 넘지 않으면서 m과 최대한 가깝게 만드는 3개의 숫자의 합을 구한다.

n, m = map(int, input().split())
num = list(map(int,input().split()))
ans = 0

def add_num(n, m):
    a = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if num[i] + num[j] + num[k] <= m:
                    a.append(num[i] + num[j] + num[k])
                    a.sort(reverse=True)
    return a[0]

add_num(n,m)