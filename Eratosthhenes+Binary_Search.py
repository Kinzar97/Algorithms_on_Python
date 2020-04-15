from Binary_search import binary_search
N = 100000
A = [True] * N
A[0] = A[1] = True
B = []
for i in range(2, N):
    if A[i]:
        for j in range(i*2, N, i):
            A[j] = False
for i in range(1, N):
    if A[i]:
        B.append(i)

print('Prime number' if type(binary_search(B, 19)) == int else 'Composite number')
