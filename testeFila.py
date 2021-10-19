from typing import Deque,Any
from collections import deque
queue: Deque[Any]=deque()
queue.append('a')
queue.append('b')
queue.append('c')
print('Removido',queue.popleft())
print('Removido',queue.popleft())
print('Removido',queue.popleft())

