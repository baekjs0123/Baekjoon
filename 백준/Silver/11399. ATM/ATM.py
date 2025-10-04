N = int(input())
Pi = list(map(int, input().split()))
Pi.sort()
Total = 0
sumNum = 0
for i in range(N):
    sumNum += Pi[i]
    Total += sumNum
print(Total)