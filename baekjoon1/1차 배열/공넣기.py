N, M = map(int, input().split())
basket = [0] * N

for t in range(M) :
    i, j, k = map(int, input().split())
    for m in range(i-1,j) :
        basket[m] = k
print(*list(basket))