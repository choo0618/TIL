import sys
sys.stdin = open('bj3006.txt','r')
#
# N=int(sys.stdin.readline())
# L = []
# for i in range(N):L.append(int(sys.stdin.readline()))
# Map,M,T = [1]*N,[],N
# s,e,tmp=1,N,1
# while tmp!=N+1:
#     r=0
#     if tmp%2:
#         for i in range(N):
#             if L[i]==s:
#                 Map[i]=0
#                 break
#             else:r+=Map[i]
#         s+=1
#     else:
#         for i in range(N-1,-1,-1):
#             if L[i]==e:
#                 Map[i]=0
#                 break
#             else:r+=Map[i]
#         e-=1
#     print(r)
#     tmp+=1


N = int(sys.stdin.readline())
L = []
tree = [0 for i in range(100002)]


def sumTree(pos):
    global tree
    pos += 1
    ret = 0
    while (pos > 0):
        ret += tree[pos]
        pos &= (pos - 1)  # 마지막 비트를 지우는 연산

    return ret


def addTree(pos, val):
    global tree
    pos += 1
    while (pos < len(tree)):
        tree[pos] += val
        pos += (pos & -pos)  # 마지막 비트를 추출


for i in range(N):
    addTree(i, 1)
    L.append([int(sys.stdin.readline()), i])

L.sort()

for i in range(N // 2):
    print(sumTree(L[i][1]) - 1)
    addTree(L[i][1], -1)
    print(sumTree(N) - sumTree(L[N - 1 - i][1]))
    addTree(L[N - 1 - i][1], -1)

if N % 2 == 1:
    print(0)
