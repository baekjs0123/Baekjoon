A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
str_mul = str(mul)
count_lst = [0] * 10
for i in range(len(count_lst)):
    for j in range(len(str_mul)):
        if i == int(str_mul[j]):
            count_lst[i] += 1
for i in range(len(count_lst)):
    print(count_lst[i])