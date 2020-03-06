import sys
sys.stdin = open('bj2844.txt','r')

H,M=map(int,input().split())
print((H-(M<45))%24,(M-45)%60)

if not H:H=24
m=60*H+M-45
print(m//60 if m//60!=24 else 0,m%60)