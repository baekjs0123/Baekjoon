import sys
#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1181                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: baekjs0123 <boj.kr/u/baekjs0123>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1181                           #+#        #+#      #+#     #
#    Solved: 2025/10/04 20:40:09 by baekjs0123    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N = int(input())
words = [sys.stdin.readline().strip() for _ in range(N)]
words = sorted(set(words), key=lambda x: (len(x), x))
for i in range(len(words)):
    print(words[i])