N = int(input())
light = list(map(int, input().split()))
student = int(input())

light_switch = []
for s in range(student) :
    m, num = map(int, input().split())

    if m == 1 :
        for i in range(1, 9) :
            if 1 <= num*i <= 8 :
                light[num*i] = 1 - light[num*i]
            
            light_switch.append(light)

    elif m == 2 :
        for i in range(1,5) :
            if light[num - i] == light[num + i] :
                light[num-i] = 1 - light[num-i]
                light[num + i] = 1- 