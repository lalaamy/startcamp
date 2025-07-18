A, B = map(int, input().split())
C = int(input())

T = A * 60 + B + C
H = (T // 60) % 24
M = T % 60

print(H, M)