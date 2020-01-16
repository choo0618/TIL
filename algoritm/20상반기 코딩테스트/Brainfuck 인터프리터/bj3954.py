import sys
sys.stdin = open('bj3954.txt','r')

T = int(input())
for t in range(T):
    M,C,I=map(int,input().split())
    L,W=input(),input()
    Arr = [0]*M
    Map = [0]*C
    tmp,num=1,0
    for idx,c in enumerate(L):
        if c=='[':
            Map[idx]=tmp
            tmp+=1
        elif c==']':
            tmp -= 1
            Map[idx]=tmp

    P,Idx,cnt,Stack=0,0,0,[]
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
            Stack.append(Idx)
            if not Arr[P]:
                tmp=Map[Idx]
                while True:
                    Idx+=1
                    if Map[Idx]==tmp:break
                cnt+=1
                continue
        elif L[Idx]==']':
            tmp = Stack.pop()
            if Arr[P]:
                Idx = tmp
                cnt+=1
                continue
        elif L[Idx]==',':
            if num<I:
                Arr[P]=ord(W[num])
                num+=1
            else:Arr[P]=255
        Idx+=1
        if Idx==C:break
        cnt+=100
    if Idx==C:print('Terminates')
    else:
        Ls = Stack[0]
        for s in range(Ls+1,C):
            if Map[Ls]==Map[s]:
                Le=s
                break
        print("Loops %d %d"%(Ls,Le))
