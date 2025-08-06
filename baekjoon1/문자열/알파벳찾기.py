T = str(input())

# [ord('a')-97]

result = [0] * 26
for i in T :
    idx = (ord(i)-97)
    result[idx] += 1
print (result)