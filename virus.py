# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수 - 간선의 수
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력

# DFS를 이용해 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 구하는 코드
def dfs(graph, v, visited):
    global count  # 전역 변수를 사용해 감염된 컴퓨터 수를 기록
    visited[v] = True  # 현재 노드를 방문 처리
    count += 1  # 감염된 컴퓨터 수를 증가
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 컴퓨터 수 입력
computer = int(input())

# 연결된 쌍의 수 입력
k = int(input())

# 그래프 초기화
graph = [[] for _ in range(computer + 1)]

# 네트워크 상의 연결 정보 입력
for _ in range(k):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 연결이므로 양쪽에 추가

# 각 컴퓨터의 연결 리스트를 오름차순으로 정렬
for i in range(1, computer + 1):
    graph[i].sort()

# 방문 여부를 기록할 리스트 초기화
visited = [False] * (computer + 1)

# 감염된 컴퓨터 수 (1번 컴퓨터는 감염된 상태에서 시작하기 때문에 초기값은 -1)
count = -1

# DFS 수행 (1번 컴퓨터에서 시작)
dfs(graph, 1, visited)

# 결과 출력 (1번 컴퓨터를 제외한 감염된 컴퓨터의 수 출력)
print(count)
