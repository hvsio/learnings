import numpy as np

n, m = input().split(" ")

a = np.array([[entry for entry in input().split(" ")] for _ in range(int(n))], int)
b = np.array([[entry for entry in input().split(" ")] for _ in range(int(n))], int)
print(f"{a+b}\n{a-b}\n{a*b}\n{a//b}\n{a%b}\n{a**b}")
