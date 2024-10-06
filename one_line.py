# 사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억한다. N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다.
# 각 사람들이 기억하는 정보가 주어질 때, 줄을 어떻게 서야 하는지 출력하는 프로그램

# 첫번째 줄에는 사람의 수가 주어잠. N은 10이하의 자연수
num = int(input())
if num > 10 or num <= 0:
    print("사람 수는 10 이하의 자연수여야 합니다.")
    exit()

# 두번째 줄에서는 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명 있었는지 
# i번째 수는 0보다 크거나 같고, N-i보다 작거나 같다. i는 0부터 시작

# 딕셔너리에 키 값 i에 왼쪽의 사람 수 n을 데이터 저장
people = []
people = list(map(int, input("").split()))

sort_list = [None] * num

# 각 사람을 그들이 기억하는 대로 줄을 세운다.
for i in range(num):
    left_taller_count = people[i]  # i번째 사람보다 큰 사람이 왼쪽에 몇 명 있었는지
    # position = 0

    # 줄을 돌면서 사람을 배치할 빈 자리를 찾는다
    for j in range(num):
        if sort_list[j] is None:  # 빈 자리를 찾으면
            if left_taller_count == 0:  # 남은 큰 사람이 없으면 여기에 배치
                sort_list[j] = i + 1  # i + 1이 사람의 키(1부터 N까지)
                break
            else:
                left_taller_count -= 1  # 빈 자리인데 아직 왼쪽에 더 큰 사람이 있어야 함

# 결과 출력
print(*sort_list)  # 리스트를 공백으로 구분하여 출력