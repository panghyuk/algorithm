from collections import deque

def bfs(graph,start,visit):
    # 큐 구현을 위해 deque 라이브러리 사용
    que = deque([start])
    # 현재 노드 방문 처리
    visit[start] = True

    # 큐가 빌 때까지 반복
    while que:
        v = que.popleft()
        print(v, end = ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visit[i]:
                que.append(i)
                visit[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (index 0은 사용 X)
visit = [False] * 9

bfs(graph, 1, visit)