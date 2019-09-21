# def solution(answers):
#     answer = [0,0,0,0]
#     result=[]
#     first = []
#     second = []
#     third = []
#     n = 0
#     while n!=len(answers):
#         if not n%5:
#             first += [1,2,3,4,5]
#         if not n%8:
#             second += [2,1,2,3,2,4,2,5]
#         if not n%10:
#             third += [3,3,1,1,2,2,4,4,5,5]
#         if answers[n] == first[n]:
#             answer[1] += 1
#         if answers[n] == second[n]:
#             answer[2] += 1
#         if answers[n] == third[n]:
#             answer[3] += 1
#         n+=1
#     for r in range(4):
#         if max(answer)==answer[r]:
#             result.append(r)
#     return result
# print(solution([1,2,3,4,5]))

# month=[0,31,29,31,30,31,30,31,31,30,31,30,31]
# day=sum(month[0:3])+1
# print(day)

import itertools
#
#
# def Prime(x):
#     for n in range(2, x):
#         if not x % n:
#             return False
#     return True
# def solution(numbers):
#     number = list(map(str, list(str(numbers))))
#     R = set()
#     Per = []
#     for p in range(1, len(number) + 1):
#         Per.append(list(itertools.permutations(number, p)))
#     for P1 in Per:
#         for P2 in P1:
#             Number = int(''.join(P2))
#             if Number and Number != 1 and Prime(Number):
#                 R.add(Number)
#     return len(R)
# R=solution("011")
# print(R)

# def solution(priorities, location):
#     R=0
#     while True:
#         if priorities[0]!=max(priorities):
#             priorities.append(priorities.pop(0))
#         else:
#             R+=1
#             priorities.pop(0)
#             if not location:break
#         location-=1
#         if location == -1: location = len(priorities)-1
#     return R
# print(solution([1,1,9,1,1,1],0))

# def DFS(List,words):
#     if sum(List)==len(List):return
#     for i in range(len(List)):
#         if List[i]: continue
#         else:
#             List[i]=1
#             if List in words:
#                 DFS(List,words)
#                 return
#             else:List[i]=0
#
# def solution(begin, target, words):
#     if not target in words: return 0
#     for w in range(len(words)):
#         check = [0] * len(target)
#         for c in range(len(target)):
#             if target[c] == words[w][c]:
#                 check[c] = 1
#         words[w] = check
#     Begin = [0]*len(begin)
#     R = 0
#     r = len(begin)+1
#     for b in range(len(begin)):
#         if begin[b]==target[b]:
#             Begin[b]=1
#             r-=1
#     DFS(Begin,words)
#     if sum(Begin)==len(begin):R=r
#     return R
# print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log', 'cog']))

# def DFS(n,hyo):
#     if hyo>n:return
#     if n==hyo:
#         return
#     DFS(n,hyo+1)
#     DFS(n,hyo+2)
#
# def solution(n):
#     R=0
#     DFS(n,0)
#     return R
# print(solution(4))

# def solution(number, k):
#     R = ''
#     # n = 0
#     while k:
#         check = 1
#         for c in range(0,k+1):
#             if number[0]<number[c]:
#                 k -= 1
#                 check = 0
#                 break
#         if check:
#             R += number[0]
#         # n+=1
#         number = number[1:len(number)]
#         if len(number)==k:
#         # if len(number)-n == k:
#             number = ''
#             break
#     R += number
#     print(R)
#     return R

# def solution(number, k):
#     R=[]
#     for n in number:
#         R.append(n)
#         if len(R)>1 and k:
#             i = len(R)-1
#             while i:
#                 if R[i]>R[i-1]:
#                     R[i],R[i-1] = R[i-1],R[i]
#                     R.pop()
#                     k-=1
#                     if not k:break
#                 else:break
#                 i-=1
#     if k:R=R[:len(R)-k]
#     print(R)
#     return R
# solution('2222',2)


# def solution(progresses, speeds):
#     r =  0
#     R = []
#     while progresses:
#         for p in range(len(progresses)):
#             progresses[p] += speeds[p]
#
#         if progresses[0] == 100:
#             R.append(0)
#             while progresses and progresses[0]>=100:
#                 R[r]+=1
#                 progresses.pop(0)
#             r+=1
#     print(R)
#     return R

# def solution(progresses, speeds):
#     day=[0]*len(progresses)
#     R=[1]
#     for d in range(len(day)):
#         day[d] = (100-progresses[d])//speeds[d]
#         if progresses[d] + day[d]*speeds[d] < 100:
#             day[d] += 1
#     c,i,r = 0,1,0
#     while True:
#         if day[c] >= day[i]:
#             R[r] += 1
#         else:
#             R.append(1)
#             r+=1
#             c= i
#         if i == len(progresses)-1:
#             break
#         i += 1
#     print(day)
#     print(R)
#     return None
# solution([93,30,55,90,30,55],[1,30,5,1,30,5])

def solution(bridge_length, weight, truck_weights):
    Time = 0
    L, Arr = len(truck_weights), 0
    bridge = [0] * (bridge_length + 1)
    while True:
        if bridge[-1]:
            Arr+=1
            bridge[-1]=0
        if Arr==L:break
        if truck_weights and sum(bridge)+truck_weights[0] <= weight:
            bridge[0] = truck_weights.pop(0)
        bridge.insert(bridge.pop(),0)
        Time += 1
    print(Time+1)
    return Time+1

solution(100,100,[10,10,10,10,10,10,10,10,10,10])

