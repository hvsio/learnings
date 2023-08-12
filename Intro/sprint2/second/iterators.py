import itertools

nr, letters, tuple_size = int(input()), input().split(" "), int(input())
combs = list(itertools.combinations(letters, tuple_size))
combs_a = list(filter(lambda x: 'a' in x, combs))
print("{:.3f}".format(len(combs_a)/len(combs)))

