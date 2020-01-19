import sys
sys.stdin = open('bj1532.txt','r')


def solution():
    G1,S1,B1=map(int,input().split())
    G2,S2,B2=map(int,input().split())
    R=0
    M = [G1-G2,S1-S2,B1-B2]
    for idx,m in enumerate(M):
        if idx==0 and m<0:
            M[1]-=abs(M[0])
            R+=abs(M[0])
            M[0]=0
        elif idx==1 and m<0:
            if M[0]:
                M[1]+=9*M[0]
                R+=M[0]
                if M[1]>=0:
                    M[0]=M[1]//9
                    R-=M[1]//9
                    M[1]-=M[0]*9
            if M[1]<0:
                M[2]-=11*abs(M[1])
                R+=abs(M[1])
                M[1]=0
        elif idx==2:
            if m>=0:return R
            else:
                if M[1]:
                    M[2]+=9*M[1]
                    R+=M[1]
                    if M[2]>=0:return R-M[2]//9
                if M[1]<0:
                    if M[0]:
                        M[2]+=81*M[0]
                        R+=2*M[0]
                        if M[2]>=0:return R-M[2]//81
                    else:return -1

print(solution())