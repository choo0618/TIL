import sys
sys.stdin = open('bj10597.txt','r')

def DFS(idx,Max,List):
    global Chk
    if idx==Len:
        if len(List)==Max:
            Chk=1
            print(' '.join(List))
        return
    if Max>50 or S[idx]=='0':return
    for n in range(1,3):
        if idx+n>Len:return
        s=S[idx:idx+n]
        if s in List:continue
        List.append(s)
        DFS(idx+n,max(Max,int(s)),List)
        if Chk:return
        List.pop()
S=input()
Len=len(S)
Chk=0
DFS(0,0,[])
