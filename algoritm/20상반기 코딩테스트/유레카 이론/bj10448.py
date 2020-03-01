import sys
sys.stdin = open('bj10448.txt','r')

def Solution():
    for i in range(44):
        for j in range(44):
            for k in range(44):
                if M[i]+M[j]+M[k]==N:return 1
    return 0
M=[0]*44
for m in range(1,45):M[m-1]=m*(m+1)//2
for t in range(int(input())):
    N=int(input())
    print(Solution())