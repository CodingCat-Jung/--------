from collections import deque

# 장마철에 특정 지역의 높이 정보가 주어졌을 때, 물에 잠기지 않는 안전한 영역의 최대 개수를 계산
# 이 함수는 BFS(너비 우선 탐색)를 사용해 높이 정보를 분석하고, 강수량을 변화시키며 가능한 모든 상황에서 안전한 영역을 계산
def find_safe_areas(N, height_map):

    # 특정 지점 (x, y)에서 시작하여 연결된 안전한 영역을 탐색
    def bfs(x, y, visited, rain_height):
        queue = deque([(x, y)])
        visited[x][y] = True
        
        while queue:
            cx, cy = queue.popleft() # 큐에서 현재 탐색할 지점을 가져옴
            
            # 상하좌우로 인접한 위치를 확인
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                # 인접한 위치 계산
                nx, ny = cx + dx, cy + dy

                # 지도 범위 내에 있고, 방문하지 않았으며, 물에 잠기지 않은 영역인지 확인
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and height_map[nx][ny] > rain_height:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    max_safe_areas = 0 # 안전한 영역의 최대 개수를 저장할 변수
    max_height = max(map(max, height_map)) # 지도에서 가장 높은 높이를 찾음
    
    # 가능한 모든 강수량(rain_height)을 기준으로 반복
    for rain_height in range(max_height + 1):
        visited = [[False] * N for _ in range(N)]
        safe_areas = 0
        
        for i in range(N):
            for j in range(N):
                # 현재 위치가 방문하지 않았고 물에 잠기지 않았다면 BFS 시작
                if not visited[i][j] and height_map[i][j] > rain_height:
                    bfs(i, j, visited, rain_height)
                    safe_areas += 1
        
        max_safe_areas = max(max_safe_areas, safe_areas)
    
    return max_safe_areas # 최대 안전한 영역 개수를 반환


n = int(input())
zone = [list(map(int, input().split())) for _ in range(n)]  # 공백으로 구분된 높이 정보를 입력받아 2차원 리스트 생성

print(find_safe_areas(n, zone))