from itertools import combinations

s, n = input().split()
combs = [c for i in range(int(n)) for c in combinations(sorted(s), i+1)]
for c in combs: print("".join(c))