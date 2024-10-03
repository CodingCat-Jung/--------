# 스위치의 개수 받음 - 100이하 양의 정수
count = int(input(""))
if count > 100 or count <= 0:
    print("100이하의 양의 정수를 입력하시오.")
    exit()

# 각 스위치의 상태가 주어짐
switch = list(map(int, input().split()))

# 학생 수가 주어짐 - 100이하 양의 정수
student = int(input(""))
if student > 100 or student <= 0:
    print("100이하의 양의 정수를 입력하시오.")
    exit()

# 한 줄씩 한 학생의 성별, 학생이 받은 수
for _ in range(student):
    sex, num = map(int, input().split())

    # 남자는 1
    if sex == 1:
        for i in range(num - 1, count, num):  
            if switch[i] == 1:
                switch[i] = 0 
            else: 
                switch[i] = 1  

    # 여자는 2
    elif sex == 2:
        num -= 1  # 인덱스를 맞추기 위해 1 감소
        left = right = num

        # 본인 스위치 변경
        if switch[num] == 1:
            switch[num] = 0 
        else: 
            switch[num] = 1

        while left > 0 and right < count - 1:  # 좌우 대칭 체크

            left -= 1
            right += 1

            if switch[left] == switch[right]:

                if switch[left] == 1:
                    switch[left] = 0 
                else: 
                    switch[left] = 1

                if switch[right] == 1:
                    switch[right] = 0 
                else: switch[right] = 1

            else: break

# 스위치 출력
# 스위치 상태를 1번 스위치부터 한 줄에 20개씩 출력
for i in range(count):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:  # 20개마다 줄바꿈
        print()

# 마지막 줄 처리 (만약 스위치가 20의 배수가 아닌 경우 남은 부분 출력)
if count % 20 != 0:
    print()