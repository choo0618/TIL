import sys
sys.stdin = open("input.txt","r")

# L=[int(x) for x in input().split()]
# print(L)
# r1=1
# r2=1
# while L[0] and L[1]:
#     for x in range(2,18):
#         if not L[0]%x and not L[1]%x:
#             r1*=x
#             r2*=x
#             L[0] = L[0] // x
#             L[1] = L[1] // x
#             break
# r2*=(L[0]*L[1])
def prime(n):
    if n<2:return False
    for i in range(2,n//2+1):
        if n%i==0:return False
    return True
a,b=map(int,input().split())
for x in range(a,b+1):
    # for y in range(1,(x+1)//2+1):
    #     if x==1:break
    #     if not x%y:
    #         cnt+=1
    #     if cnt==2:
    #         break
    if prime(x):
        print(x)