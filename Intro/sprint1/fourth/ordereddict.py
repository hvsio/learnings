from collections import OrderedDict

od = OrderedDict()
for n in range(int(input())):
    *name, price = input().split()
    od[" ".join(name)] += int(price)
for it in od.items(): print("%s %d" % it)
    