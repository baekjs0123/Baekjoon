#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11047                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: baekjs0123 <boj.kr/u/baekjs0123>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11047                          #+#        #+#      #+#     #
#    Solved: 2025/10/04 21:32:49 by baekjs0123    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N, K = map(int, input().split())
Ai = [int(input()) for _ in range(N)]
Ai.sort(reverse=True)
answer = 0
for i in range(N):
    coinCount = 0
    if K > 0 and Ai[i] <= K:
        coinCount = K // Ai[i]
        answer += coinCount
        K -= Ai[i] * coinCount
print(answer)
