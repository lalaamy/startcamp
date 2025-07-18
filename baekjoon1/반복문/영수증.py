X = int(input())
N = int(input())
numbers = 0

for i in range(N) :
    a, b = map(int, input().split())
    numbers += a * b

if numbers == X :
    print("Yes")
else :
    print("No")
    