N = int(input())

switch = [0] + list(map(int, input().split()))
student = int(input())

for _ in range(student) :
    gender, number = map(int, input().split())

    if gender == 1 : # 남자일 때
        for i in range(number, N+1, number) :
            switch[i] = 1 - switch[i]
            # continue

    if gender == 2 : # 여자일 때
        i = 0
        while 1 <= number -i <= N and 1 <= number +i <= N and switch[number-i] == switch[number+i] :
            i += 1
        i -= 1

        for j in range (number-i, number+i+1) :
            switch[j] = 1 - switch[j]
            # switch[number-i] = 1 - switch[number-i]
            # switch[number+i] = 1 - switch[number+i]

# for p in range(len(switch)) :
#     print(switch[p], end=' ')
#     if p % 20 == 0:
#         print() 

idx = 1
while idx < len(switch):
    print (*switch[idx:idx+20])
    idx += 20