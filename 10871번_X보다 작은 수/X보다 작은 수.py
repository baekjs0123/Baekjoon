#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10871                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: baekjs0123 <boj.kr/u/baekjs0123>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10871                          #+#        #+#      #+#     #
#    Solved: 2025/10/04 19:56:03 by baekjs0123    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N, X = map(int, input().split())
numbers = list(map(int, input().split()))
answer = []
for i in range(N):
    if numbers[i] < X:
        answer.append(numbers[i])
print(*answer)