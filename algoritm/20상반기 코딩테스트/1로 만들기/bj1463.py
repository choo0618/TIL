import sys
sys.stdin=open('bj1463.txt','r')

import heapq
N=int(input())
Map=[987654321]*(N+1)
Map[N]=0
Que=[(0,N)]
while Que:
    cnt,n=heapq.heappop(Que)
    if n==1:print(cnt);break
    cnt+=1
    if not n%3:
        nN=n//3
        if cnt<Map[nN]:
            Map[nN]=cnt
            heapq.heappush(Que,(cnt,nN))
    if not n%2:
        nN=n//2
        if cnt<Map[nN]:
            Map[nN]=cnt
            heapq.heappush(Que,(cnt,nN))
    if cnt<Map[n-1]:
        Map[n-1]=cnt
        heapq.heappush(Que,(cnt,n-1))



dictionary = {}


def calculate(n):
    if n <= 1:
        return 0
    else:
        global dictionary
        if n in dictionary:
            return dictionary[n]
        else:
            templist = []
            templist.append(calculate(n // 3) + n % 3 + 1)
            templist.append(calculate(n // 2) + n % 2 + 1)
            dictionary[n] = min(templist)
            return dictionary[n]


X = int(input())
print(calculate(X))