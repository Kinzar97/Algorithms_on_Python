N = 100
A = [True] * N
A[0] = A[1] = True
for i in range(2, N):
    if A[i]:
        for j in range(i*2, N, i):
            A[j] = False
for i in range(N):
    print(i, '-', 'Простое' if A[i] else 'Составное')
