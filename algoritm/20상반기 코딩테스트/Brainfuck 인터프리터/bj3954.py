import sys
sys.stdin = open('bj3954.txt','r')

T = int(input())
for t in range(T):
    M,C,I=map(int,input().split())
    L,W=input(),input()
    Arr = [0]*M
    num=0
    bascket={}
    for c in range(C):
        if L[c]=='[':
            tmp = 0
            for c1 in range(c+1,C):
                if L[c1]=='[':tmp+=1
                elif L[c1]==']':
                    if not tmp:
                        bascket[c]=(c,c1)
                        bascket[c1]=(c,c1)
                        break
                    else:tmp-=1
    P,Idx,cnt,Stack,Max=0,0,0,[],0
    while cnt<50000001:
        if L[Idx]=='-':
            Arr[P]-=1
            if Arr[P]==-1:Arr[P]=255
        elif L[Idx]=='+':
            Arr[P]+=1
            Arr[P]%=256
        elif L[Idx]=='<':
            P-=1
            if P==-1:P=M-1
        elif L[Idx]=='>':
            P+=1
            P%=M
        elif L[Idx]=='[':
            if not Arr[P]:
                Idx = bascket[Idx][1]
                cnt+=1
                continue
        elif L[Idx]==']':
            if Arr[P]:
                Idx = bascket[Idx][0]
                cnt+=1
                continue
        elif L[Idx]==',':
            if num<I:
                Arr[P]=ord(W[num])
                num+=1
            else:Arr[P]=255
        Idx+=1
        if Idx>Max:Max=Idx
        if Idx==C:break
        cnt+=1
    if Idx==C:print('Terminates')
    else:print('Loop %d %d'%(bascket[Max][0],bascket[Max][1]))