import sys
sys.stdin = open('A+B.txt','r')

print(sum(list(map(int,input().split()))))

R=int(input())
print(R+int(input()))

for t in range(int(input())):
    print(sum(list(map(int, input().split()))))

while True:
    try:print(sum(list(map(int, input().split()))))
    except:break

while True:
    R=sum(list(map(int, input().split())))
    if not R:break
    print(R)

for t in range(int(input())):
    print(sum(list(map(int,input().split(',')))))

for t in range(int(input())):
    print('Case #%d: %d'%(t+1,sum(list(map(int,input().split())))))

for t in range(int(input())):
    a,b=map(int,input().split())
    print('Case #%d: %d + %d = %d'%(t+1,a,b,a+b))

print(sum(list(map(int,input().split()))))