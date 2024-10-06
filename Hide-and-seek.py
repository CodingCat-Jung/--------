# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수

# 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램

# BFS 탐색법 사용
# BFS는 모든 경로를 동시에 탐색하고, 먼저 도착하는 경로가 가장 빠르다는 특성을 이용하여 최단 시간을 구함
from collections import deque # 양방향 큐

def find_brother(N, K):
    if N == K:
        return 0  # 수빈이와 동생이 같은 위치에 있을 경우

    # BFS를 위한 큐 생성 (위치, 시간) - 튜플로 묶어서 queue에 저장
    queue = deque([(N, 0)])
    visited = [False] * 100001  # 0부터 100000까지 방문 여부 기록 배열
    visited[N] = True

    while queue:

        current, time = queue.popleft()

        # 세 가지 이동 방법을 모두 고려
        for next_pos in (current - 1, current + 1, current * 2):

            # 다음 위치(next_pos)가 0 이상 100000 이하 허용 범위 내 and 아직 방문하지 않은 위치
            if 0 <= next_pos <= 100000 and not visited[next_pos]:

                if next_pos == K:
                    return time + 1  # 동생을 찾은 경우 시간을 반환
                
                queue.append((next_pos, time + 1)) # 큐에 위치와 시간 업데이트
                visited[next_pos] = True  # 방문 표시

    return -1  # 도달할 수 없을 경우 (이론상 불가능)

# 입력 받기
N, K = map(int, input().split())

# 결과 출력
print(find_brother(N, K))
