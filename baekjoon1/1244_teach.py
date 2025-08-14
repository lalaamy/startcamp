'''
필요 데이터
N : 스위치 수
switches : 스위치의 상태 (입력 받기)
M : 명령의 수
gender : 명령의 성별
number : 명령의 번호
idx : 남자 명령일 때 몇 배수인지 체크 용도
l, r : 여자 명령을 수행하는 경우, 좌측 인덱스와 우측 인덱스
'''
'''
로직

1. N, switches, M 입력
2. M줄에 걸쳐 명령 입력 받기 (for문 사용)
    ㄱ. 남자일 때
        - number부터 배수에 대하여 상태를 스왑해주기
        
    ㄴ. 여자일 때
        - number 변경 (가운데 수)
        - 좌 우 대칭 ( l지점과 r지점의 값이 같을 때 )
          해당 지점의 값을 스왑
        - l, r 지점 갱신
'''

N = int(input())
switches = list(map(int, input().split()))
switches.insert(0, 0)

M = int(input())
for _ in range(M) :
    gender, number = map(int, input().split())

    if gender == 1 :
        idx = 1
        while number * idx <= N :
            switches[number*idx] = (switches[number*idx]+1) % 2
            idx += 1

    else :
        switches[number] = (switches[number]+1) % 2
        l, r = number-1, number+1

        while 1 <= l and r <= N and switches[l] == switches[r] :
            switches[l] = (switches[l]+1) % 2
            switches[r] = (switches[r]+1) % 2
            l -= 1
            r += 1

i = 1
while i <= N :
    print(*switches[i:i+20])
    i += 20

# for i in range(1, N+1) :
#     print (switches[i], end= ' ')
#     if i % 20 == 0 :
#         print ()