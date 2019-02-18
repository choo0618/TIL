import sys

sys.stdin = open('input.txt', 'r')# 파일에서 읽을 때 사용

# Flatter
# for num in range(10):
#     N = int(input())
#     L = list(map(int, input().split()))
#     L.sort(reverse=True)
#     for n in range(N):
#         L[0] -= 1
#         L[-1] += 1
#         L.sort(reverse=True)
#     result = max(L)-min(L)
#     print("#%d %d"%(num+1,result))

# min,max
# TC=int(input())
# for num in range(1,TC+1):
#     N = int(input())
#     L = list(map(int, input().split()))
#     result = max(L)-min(L)
#     print("#%d %d"%(num,result))

# 숫자카드
# TC=int(input())
# for num in range(1,TC+1):
#     N = int(input())
#     L = list(map(int, input(str())))
#     counting = [0] * (max(L)+1)
#     for c in range(len(L)):
#         counting[L[c]] += 1
#     a=0
#     for m in range(len(counting)):
#         if counting[m]>=a:
#             a=counting[m]
#             result = m
#             count = counting[m]
#     print("#%d %d %d"%(num,result, count))

# 구간합
# TC=int(input())
# for num in range(1,TC+1):
#     M = list(map(int, input().split()))
#     L = list(map(int, input().split()))
#     max1=0
#     min1=987654321
#     for i in range(M[0]-M[1]+1):
#         # a = sum(x for x in range(L[i],L[i+M[1]]))  #L7 L8 L9
#         a = 0
#         for s in range(M[1]):
#             a += L[i+s]
#         if a>max1:
#             max1=a
#         if a<min1:
#             min1=a
#     result = max1-min1
#     print("#%d %d"%(num,result))

# 전기버스
# TC=int(input())
# for num in range(1,TC+1):
#     M = list(map(int, input().split()))
#     L = list(map(int, input().split()))
#     cnt = 0
#     stop = [0] * M[1]
#     for c in range(len(L)):
#         stop[L[c]] += 1
#     now = M[0]
#     before=0
#     while M[1]>now:
#         if stop[now]:
#             before = now
#             now += M[0]
#             cnt += 1
#         else:
#             now -= 1
#             if now == before:
#                 cnt = 0
#                 break
#     print("#%d %d"%(num, cnt))

