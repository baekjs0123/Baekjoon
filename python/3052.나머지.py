# 10개의 숫자를 입력받아 리스트에 저장합니다.
numbers = [int(input()) for _ in range(10)]

# 나머지를 저장할 집합을 생성합니다.
remainders = set()

# 입력받은 숫자들을 순회하며 42로 나눈 나머지를 집합에 추가합니다.
for number in numbers:
    remainder = number % 42
    remainders.add(remainder)

# 집합의 크기가 서로 다른 나머지 값의 개수이므로 이를 출력합니다.
print(len(remainders))


# 분명 답이 다 맞는데 계속 틀렸다고 함....ㅠ
# numbers = [int(input()) for _ in range(10)]
# cnt = 0
# duplicate_count = 0
# remainder = []
# for i in range(len(numbers)):
#     remainder.append(numbers[i] % 42)
# for i in range(len(remainder)):
#     cnt = 0
#     for j in range(len(remainder)):
#         if remainder[i] != remainder[j]:
#             cnt += 1
            
#     if cnt != len(remainder) - 1:
#         duplicate_count += 1
# if cnt == 0:
#     result = 1
#     print(result)
# else:
#     result = int(len(remainder) - duplicate_count / 2)
#     print(result)
