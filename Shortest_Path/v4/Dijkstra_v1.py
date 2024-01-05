import sys
input = sys.stdin.readline
INF = int(1e9)

#노드, 간선의 개수
n, m = map(int, input().split())
#시작 노드 번호
start = int(input())
#노드 연결정보를 위한 리스트
graph = [[] for i in range(n+1)]
#방문여부 체크 리스트
visited = [False] * (n+1)
#최단거리 테이블
distance = [INF] * (n+1)

#간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c다.
    graph[a].append((b,c))

    #방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
def dijkstra(start):
    #시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작노드를 제외한 전체 n-1노드에 대해서 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
dijkstra(start)

#모든 노드로 가기 위한 최단거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
