my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positiv_numder = []
a = 0
while a < len(my_list):
    if my_list[a] == 0:
        a += 1
        continue
    if my_list[a] <= 0:
        break
    positiv_numder.append(my_list[a])
    a += 1
print(positiv_numder)