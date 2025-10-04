#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11399                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: baekjs0123 <boj.kr/u/baekjs0123>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11399                          #+#        #+#      #+#     #
#    Solved: 2025/10/04 21:11:13 by baekjs0123    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())
Pi = list(map(int, input().split()))
Pi.sort()
Total = 0
sumNum = 0
for i in range(N):
    sumNum += Pi[i]
    Total += sumNum
print(Total)