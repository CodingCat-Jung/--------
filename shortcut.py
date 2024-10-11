# 첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다. 
# 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다. 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 
# 지름길의 시작 위치는 도착 위치보다 작다.

# 입력 받기
N, D = map(int, input().split())

# 지름길 정보 저장
shortcut_list = []

for _ in range(N):
    start, finish, length = map(int, input().split())
    if finish <= D:  # 지름길의 도착점이 고속도로의 길이보다 작을 때만 유효
        shortcut_list.append((start, finish, length))

# distance 배열 - 최소 거리 기록. 0부터 D까지의 거리 테이블, 초기에는 각 지점까지의 거리를 기본적으로 1씩 더해서 가는 값으로 설정
# distance = [0, 1, 2, 3, 4, ... , D-1, D]
distance = list(range(D + 1))

# 0부터 D까지 한 칸씩 이동하면서 지름길을 적용해 최소 거리를 계산
for i in range(D + 1):

    # 먼저 현재 지점으로 지름길 타고 온 경우 다음 지점으로 1칸 이동하는 경우의 최소 거리 갱신
    if i < D:
        distance[i + 1] = min(distance[i + 1], distance[i] + 1)
    
    # 현재 지점에서 시작하는 지름길을 적용 - 지름길 리스트 탐색
    for start, finish, length in shortcut_list: 

        # 현재 지점에서 finish 지점까지 가는 지름길이 존재하는 경우
        if i == start and finish <= D: 
            distance[finish] = min(distance[finish], distance[i] + length) # finish 지점 거리 최신화

# 결과 출력: D까지의 최소 거리
print(distance[D])
