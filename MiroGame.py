# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동

# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)
# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력

from collections import deque

# 상하좌우 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# maze는 BFS를 통해 탐색하면서 각 칸까지 도달할 수 있는 최단 거리를 기록하는 배열로 변환
def bfs_maze(N, M, maze):
    # BFS를 위한 큐 생성, 시작점 (0, 0)부터 시작 (1, 1이지만, 배열은 0-index)
    queue = deque([(0, 0)])
    
    # 방문 기록을 위한 visited 배열 (방문한 칸은 다시 방문하지 않음)
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        # 네 방향에 대해 이동 시도 (상, 하, 좌, 우)
        for i in range(4):
            
            # nx, ny는 현재 칸 (x, y)에서 네 가지 방향으로 이동한 칸의 좌표를 계산한 값
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위 내에 있는지 확인
            if 0 <= nx < N and 0 <= ny < M:

                # 이동할 수 있고 방문하지 않은 곳일 경우
                if maze[nx][ny] == 1 and not visited[nx][ny]:

                    # 이동한 곳은 이동 횟수를 기록 (지금까지 온 거리 + 1)
                    maze[nx][ny] = maze[x][y] + 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    # 마지막 칸까지의 이동 횟수를 반환 (도착지점은 N-1, M-1)
    return maze[N-1][M-1]

# 입력 받기
N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]

# BFS를 통해 최소 칸 수 찾기
result = bfs_maze(N, M, maze)
print(result)
