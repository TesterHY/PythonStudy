"""
그래프의 탐색

하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한번씩 방문
그래프의 가장 기본적인 연산
많은 문제들이 단순히 그래프의 노드를 탐색하는 것으로 해결
  도로망에서 특정 도시에서 다른 도시로 갈 수 있는지 여부
  전자회로에서 특정 단자와 다른 단자가 서로 연결되어 있는지 여부

가장 일반적인 두 가지 알고리즘
 - 너비우선탐색(Breadth-First-Search, BFS)
 - 깊이우선탐색(Depth-First-Search, DFS)

정점들을 서치한느 동안, 방문된 정점들을 기억하고 있어야 함
 - 가장 일반적인 방법은 마킹
 - 흰색:미방문(unseen), 회색:방문중(seen),검정:방문끝(Completed)

그래프 탐색 응용
 Web crawling
 Social networking
 Network broadcast
 Garbage collection
 Model checking
 Solving puzzles
 Etc.

"""