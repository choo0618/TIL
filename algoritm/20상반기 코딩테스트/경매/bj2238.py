import sys
sys.stdin = open('bj2238.txt','r')

U,N=map(int,input().split())
Map = [[]for m in range(U+1)]
for _ in range(N):
    name,price = map(str,input().split())
    Map[int(price)].append(name)
Min = min(len(m)for m in Map if m)
for idx,p in enumerate(Map):
    if len(p)==Min:
        print(p[0],idx)
        break

