import sys
sys.stdin = open('bj1614.txt','r')

Dic={4:0,3:1,2:2}
F = [1,2,3,4,5,4,3,2]
Hurt = int(input())
N = int(input())
if Hurt == 1:print(8*N)
elif Hurt == 5:print(8*N+4)
else:
    R = 8*(N//2)
    if N%2:R+=5+Dic[Hurt]
    else:R+=Hurt-1
    # N=1
    # for f in F:
    #     if Hurt==f and not N:break
    #     elif Hurt==f:N=0
    #     R+=1
    print(R)
