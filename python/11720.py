# for문에 리스트를 통으로 집어넣어 더하는 법
count = int(input())
num_list = list(map(int, list(input())))
num_sum = 0
for i in num_list:
    num_sum += i
print(num_sum)

# for문에 인덱스로 접근하여 계산하는 법
count = int(input())
num_list = list(map(int, list(input())))
num_sum = 0
for i in range(count):
    num_sum += num_list[i]
print(num_sum)

# sum함수 사용하여 계산하는 법.
# 반복문을 돌리지 않아 코드의 가독성과 간결함 측면에서 더 우수함.
count = int(input())
num_list = list(map(int, list(input())))
num_sum = sum(num_list)
print(num_sum)

# number를 문자열로 받아 반복문을 돌리고 정수로 형변환하여 sum함수를 활용하여 출력하는 법.
count = int(input())
num = input()

num_sum = sum(int(a) for a in num)
print(num_sum)

# number를 문자열로 받아 반복문을 돌리고 정수로 형변환하여 출력하는 법(반복문을 풀어서 쓴 버전).
count = int(input())
num = input()
num_sum = 0
for c in num:
    num_sum += int(c)
print(num_sum)