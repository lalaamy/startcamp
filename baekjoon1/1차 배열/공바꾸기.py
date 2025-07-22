N, M = map(int, input().split())
basket = [0] * N

for m in range(M) : 
    i, j = map(int, input().split())
    i, j = j, i
print(*list(basket))