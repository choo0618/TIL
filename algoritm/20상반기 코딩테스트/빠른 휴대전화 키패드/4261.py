import sys
sys.stdin = open('4261.txt','r')

# Dic=[0,0,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
Dic={'a':2,'b':2,'c':2,'d':3,'e':3,'f':3,'g':4,'h':4,'i':4,'j':5,'k':5,'l':5,'m':6,'n':6,'o':6,'p':7,'q':7,'r':7,'s':7,'t':8,'u':8,'v':8,'w':9,'x':9,'y':9,'z':9}
for t in range(int(input())):
    S,N=map(int,input().split())
    S=str(S)
    L=input().split()
    R=0
    for l in L:
        s=''
        for c in l:s+=str(Dic[c])
        if s==S:R+=1
    print('#%d %d'%(t+1,R))