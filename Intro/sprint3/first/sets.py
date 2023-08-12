_, primary_set = int(input()), set([int(x) for x in input().split()])
for _ in range(int(input())):
    action, _ = input().split()
    temp_set = set(map(int, input().split()))
    getattr(primary_set, action)(temp_set)
print(sum(primary_set))
