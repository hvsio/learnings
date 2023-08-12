from collections import deque
d = deque()

for i in range(int(input())):
    args = input().split()
    func = getattr(d, args[0])
    if len(args) > 1: func(args[1])
    else: func()
print(*d)

