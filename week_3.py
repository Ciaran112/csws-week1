l = list(range(1000001))
print(l)

minimum = min(l)
print(minimum)

maximum = max(l)
print(maximum)

total = sum(l)
print(total)

for value in range(1,20,2):
    print(value)

j = [i for i in range(3, 31,) if i % 3 == 0 ]
print(j)
print("end of list")

for i in range(1, 11):
    print("{} cubed is {}".format(i, i ** 3))

x = slice (1, 4)
print(l[x])