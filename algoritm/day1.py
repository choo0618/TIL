import sys

sys.stdin = open('input.txt', 'r')# 파일에서 읽을 때 사용

Data = list(map(int,input().split()))
print(Data)

# max값찾기
# howmany = len(Data)
# max = Data[0]
# maxindex = -1
#
# for now in range(howmany):
#     if Data[now]>max:
#         max=Data[now]
#         maxindex=now
#
# print(max, maxindex+1)
#
#
# Gravitiy
# size = len(Data)
# jumpcnt = 8
# max = 0
# for now in range(size):
#     jumpcnt = size-now-1
#     for next in range(now+1,size):
#         if Data[next]>=Data[now]:
#             jumpcnt-=1
#     if jumpcnt>max:
#         max=jumpcnt
# print(max)
#
#
# next_permutation
# cand1 = 0
# cand2 = 0
# length = len(Data)
#
# for now in range(length-1):
#     if Data[now]<Data[now+1]:
#         cand1 = now
# cand2 = length - 1
# if cand1 == 0:
#     print("마지막 숫자입니다.")
# else:
#     while Data[cand1]>Data[cand2]:
#         cand2 -= 1
#
#     Data[cand1], Data[cand2] = Data[cand2], Data[cand1]
#     Data[cand1+1:] = Data[:cand1:-1]
#
#     print(Data)
#
#
# Bubble Sort
# all = len(Data)
# for now in range(all-1):
#     for next in range(now+1, all):
#         if Data[now]>Data[next]:
#             Data[now], Data[next] = Data[next], Data[now]
#
# print(Data)

#
# Counting Sort
# counting = [0] * (max(Data)+1)
# result = [0] * len(Data)
#
# for num in range(len(Data)):
#     counting[Data[num]] += 1
# print(counting)
#
# for num in range(1,len(counting)):
#     counting[num] +=counting[num-1]
# print(counting)
#
# for num in range(len(Data) - 1, -1, -1):
#     counting[Data[num]] -= 1
#     result[counting[Data[num]]] = Data[num]
# print(result)
# #
#
# Baby-Gin
# tri = 0
# run = 0
#
# counting = [0] * (max(Data)+1)
#
# for num in range(len(Data)):
#     counting[Data[num]] += 1
#
# print(counting)
#
# for t in range(len(counting)):
#     if counting[t] >= 3:
#         counting[t] -= 3
#         tri += 1
# for r in range(0,len(counting)-2):
#     if counting[r] == counting[r+1] == counting[r+2] >= 1:
#         run += 1
#         counting[r] -= 1
#         counting[r+1] -= 1
#         counting[r+2] -= 1
#         if counting[r] == counting[r+1] == counting[r+2] == 1:
#             run += 1
#
# if tri + run == 2:
#     print("Baby-Gin!!!")
# else:
#     print("Nothing")
#
#
# building
# for num in range(10):
#     N = int(input())
#     L = list(map(int, input().split()))
#     result = 0
#     for b in range(2,len(L)-2):
#         if L[b] > max(L[b-2], L[b-1], L[b+1], L[b+2]):
#             result += L[b] - max(L[b-2], L[b-1], L[b+1], L[b+2])
#     print("#%d %d"% (num+1,result))
