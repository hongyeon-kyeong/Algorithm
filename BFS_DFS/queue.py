'''
큐 
- 선입선출, 후입후출
- collections 모듈의 deque 자료구조 사용
- deque는 스택과 큐의 기능을 모두 할 수 있음 (리스트처럼 인덱싱, 슬라이싱은 못함)
- append() appendleft() pop() popleft()
- 스택을 구현할 때 append(), pop()
- 큐를 구현할 때 append(), popleft()
'''
from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)