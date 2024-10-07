# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향

from collections import deque

# DFS 함수 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 함수 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    # 현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        
        # 해당 원소와 연결된, 아직 방문하지 않은 노드를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



# 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
# 입력 처리
N, M, V = map(int, input().split())

# 그래프 초기화 (인접 리스트 방식 사용)
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력 받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 그래프이므로 반대 방향도 추가 - graph[u]와 graph[v] 둘 다에 서로를 추가

# 각 정점의 연결된 노드를 오름차순으로 방문하기 위해 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS와 BFS를 위한 방문 기록 리스트 초기화
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

# DFS 실행
dfs(graph, V, visited_dfs)
print()  # 줄바꿈

# BFS 실행
bfs(graph, V, visited_bfs)
