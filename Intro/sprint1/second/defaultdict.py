from collections import defaultdict

x, y = input().split(' ')
x, y = int(x), int(y)
name_a = 'A'
name_b = 'B'
d = defaultdict(list)
l = list()

for xx in range(1, x+1):
    d[input()].append(str(xx))

for yy in range(0,y): l.append(input())
for ll in l: print(' '.join(d[ll]) if ll in d.keys() else -1)