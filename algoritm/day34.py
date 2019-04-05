import sys
sys.stdin=open('input.txt','r')

# # 지희의 고장난 계산기
# def D(d,i,x):
#     if d==i+1:
#         if 0<int(x)<=N and not int(x) in C:C.append(int(x));return
#         else:return
#     for j in range(len(I)):
#         D(d+1,i,x+str(I[j]))
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     N=int(input())
#     I=[]
#     for i in range(10):
#         if L[i]:I.append(str(i))
#     C=[]
#     for j in range(len(str(N))):
#         D(0,j,'')
#     R=[]
#     print(C)
#     tmp=N
#     cnt=-1
#     # for y in C[::-1]:
#     #     if tmp%y or not tmp//y in C and y==0:continue
#     #     tmp//=y
#     #     R.append(len(str(y)))
#     #     if tmp==1:break
#     # if tmp==1:cnt=sum(R)+len(R)
#     # print('#%d %d'%(n+1,cnt))


# # 파이프 옮기기
# N=int(input())
# A=[int(x)for x in input().split()]

# # 최종평가
def GCD(y,x):
    if y<x:return GCD(x,y)
    elif x==0:return y
    return GCD(y,x%y)
def IS(y,x):
    if -1<y<L[0]+1 and -1<x<L[0]+1:return True
    return False
L=[int(x)for x in input().split()]
L1=[[int(x)for x in input().split()]for y in range(L[1])]
M=[[0]*(L[0]+1)for _ in range(L[0]+1)]
for k in range(len(L1)):
    M[L1[k][0]][L1[k][1]]=k+1
print(M)
cnt=0
A=[]
for i in range(L[0]+1):
    for j in range(L[0]+1):
        if M[i][j]:
            hy=i
            hx=j
            CM=M[:]
            CM[i][j]=0
            for yy in range(L[0]+1):
                for xx in range(L[0]+1):
                    if CM[yy][xx]:
                        ty=yy-i
                        tx=xx-j
                        cnt+=1
                        print(yy,xx)
                        while IS(hy+ty,hx+tx):
                            CM[hy+ty][hx+tx]=0
                            ty+=1
                            tx+=1

print(cnt)

