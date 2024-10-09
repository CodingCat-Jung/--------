# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램
# 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산
# 나와 아버지, 아버지와 할아버지는 각각 1촌, 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌

# 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호
# 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄 - 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호
# 각 사람의 부모는 최대 한 명만 주어진다.
# 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 
# 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력

def dfs(graph, current, target, visited, degree):
    # 현재 사람이 target이면 촌수를 리턴
    if current == target:
        return degree
    
    visited[current] = True  # 현재 사람 방문 처리
    
    # 현재 사람과 연결된 다른 사람들에 대해 탐색
    for i in graph[current]:
        if not visited[i]:  # 방문하지 않은 사람에 대해 탐색
            result = dfs(graph, i, target, visited, degree + 1)  # 촌수를 1 증가시키며 탐색

            if result != -1: # -1이 아니라는 것은 찾았다는 의미 
                return result 
    
    return -1  # target을 찾지 못하면 -1 리턴



n = int(input())

people_1, people_2 = map(int, input().split())

m = int(input())

family_list = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    family_list[x].append(y)
    family_list[y].append(x)

visited = [False] * (n + 1)

# DFS를 이용해 두 사람 간의 촌수를 계산
result = dfs(family_list, people_1, people_2, visited, 0)

# 촌수를 출력 (연결되지 않은 경우 -1 출력)
print(result)