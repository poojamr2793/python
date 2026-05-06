from collections import deque

dq = deque()

dq.append(10)
dq.append(20)
dq.appendleft(30)

# Print deque elements
print(' '.join(map(str, dq)))

# Pop from front and back
dq.popleft()
dq.pop()

# Print deque elements after pop
print(' '.join(map(str, dq)))
