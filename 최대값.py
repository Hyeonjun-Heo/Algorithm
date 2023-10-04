def find_max(A):
    max = A[0]

    for i in range(len(A)):
        if A[i] > max:
            max = A[i]
    
    return max

lst = [ 1,205,468,14,79,65]
find_max(lst)