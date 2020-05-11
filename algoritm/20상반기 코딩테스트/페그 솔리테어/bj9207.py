import sys
sys.stdin = open('bj9207.txt','r')

def IS(y,x):
    return -1<y<5 and -1<x<9
def DFS(p,cnt):
    global R,C
    Check=1
    for i in range(p):
        y,x=P[i]
        for tY,tX,Y,X in (y,x+1,y,x+2),(y+1,x,y+2,x),(y,x-1,y,x-2),(y-1,x,y-2,x):
            if IS(Y,X) and A[tY][tX]=='o' and A[Y][X]!='#':
                Check=0
                A[y][x]='.'
                P[i]=[Y,X]
                A[Y][X]='o'
                idx=P.index([tY,tX])
                P.pop(idx)
                A[tY][tX]='.'

                DFS(p-1,cnt+1)

                P.insert(idx,[tY,tX])
                A[tY][tX]='o'
                A[y][x]='o'
                P[i]=[y,x]
                A[Y][X]='.'
    if Check and p<R:R,C=p,cnt

for t in range(int(input())):
    A=[]
    P=[]
    for i in range(5):
        I=list(input())
        for j in range(9):
            if I[j]=='o':P.append([i,j])
        A.append(I)
    R,C=len(P),0
    DFS(len(P),0)
    print(R,C)


    try:input()
    except:break