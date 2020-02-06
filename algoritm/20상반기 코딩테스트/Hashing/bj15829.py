import sys
sys.stdin=open('bj15829.txt','r')

N=int(input())
R=0
for idx,i in enumerate(input()):R+=(ord(i)-96)*(31**idx)
print(R%1234567891)

