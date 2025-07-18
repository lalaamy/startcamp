A, B, C = map(int, input().split())

if A == B == C :
    H = A
    print(10000 + H*1000)
elif A == B or A == C :
    H = A
    print(1000 + H*100)
elif B == C :
    H = B
    print(1000 + H*100)
else :
    print (max(A, B, C)*100)

