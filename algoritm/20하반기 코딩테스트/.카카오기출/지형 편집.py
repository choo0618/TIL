# from collections import defaultdict
# def solution(land, P, Q):
#     Len=len(land)
#     left,right=10**9,0
#     Dic=defaultdict(int)
#     for i in range(Len):
#         for j in range(Len):
#             left,right=min(left,land[i][j],1),max(right,land[i][j])
#             Dic[land[i][j]]+=1
#     if left==right:return 0
#     def Chk(x):
#         p,q=0,0
#         for k,n in Dic.items():
#             if k>x:q+=(k-x)*n
#             else:p+=(x-k)*n
#         return P*p+Q*q
#     answer=10**12
#     while left<right:
#         mid=(left+right)//2
#         r1,r2=Chk(mid),Chk(mid+1)
#         if r1<r2:right=mid
#         elif r1==r2:answer=r1;break
#         else:left=mid+1
#         answer=min(r1,r2,answer)
#     print(answer)
#     return answer

def solution(land, P, Q):
    land=sum(land, [])
    land.sort()
    N=len(land)
    max_count=int((N*Q)/(Q+P))
    small=land[:max_count]
    big=land[max_count:]
    mid=land[max_count]
    print(land)
    print(max_count)

    return ((mid*len(small)-sum(small)))*P+(sum(big)-(mid*len(big)))*Q

solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3)

