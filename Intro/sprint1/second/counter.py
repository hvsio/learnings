from collections import Counter

shoes_nr, shoe_size, customers_nr = input(), input().split(' '), input()
l = Counter(shoe_size)

revenue = 0
for c in range(int(customers_nr)):
    size, price = input().split(' ')
    if l[size] > 0:
        revenue += int(price)
        l.subtract({size: 1})
    else: continue

print(revenue)
