# # for문 돌리는 방식
# # num을 담을 리스트 선언
# numbers= []
# # 몇번째 숫자인지 카운트할 변수 선언
# count = 0
# # 최대값을 저장한 변수 선언
# max_num = 0
# # 1 ~ 9까지 반복문 돌리기
# for i in range(1, 10):
#     num = int(input())
#     numbers.append(num)
#     if max_num < num:
#         max_num = num
#         count = i
# print(max_num)
# print(count)

# max(), index() 쓰는법
# num을 담을 리스트 선언
numbers= []
# 1 ~ 9까지 반복문 돌리기
for i in range(1, 10):
    num = int(input())
    numbers.append(num)
max_num = max(numbers)
print(max(numbers))
print(numbers.index(max_num) + 1)

