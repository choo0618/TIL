import sys
sys.stdin = open('bj1532.txt','r')

def solution():
    G1,S1,B1=map(int,input().split())
    G2,S2,B2=map(int,input().split())
    R=0
    if B2>B1:
        s=(B2-B1)//9
        if (B2-B1)%9:s+=1
        if s>S1:
            g=(s-S1)//9
            if (s-S1)%9:g+=1
            S1+=9*g
            G1-=g
            R+=g
            if G1<0:return -1
        S1-=s
        B1+=9*s
        R+=s
    if S2>S1:
        g=(S2-S1)//9
        if (S2-S1)%9:g+=1
        if g<=G1:
            G1-=g
            S1+=9*g
            R+=g
    if G1>=G2:return R
    s=(G2-G1)*11
    if s>S1:
        b=(s-S1)*11
        if B1-b<0:return -1
        B1-=b
        S1+=b//11
        R+=b//11
    G1=G2
    S1-=s
    R+=s//11
    if S1>=S2:return R
    b=(S2-S1)*11
    if b>B1:return -1
    return R+b//11

print(solution())

# if S2>S1 or B2>B1:
#     s=(B2-B1)//9
#     if (B2-B1)%9:s+=1
#     if S1-s>0:
#         B1+=9*s
#         S1-=s
#         R+=s
#     else:
#         B1 += 9 * S1
#         R += S1
#         S1 = 0
#     g=(S2-S1)//9
#     if (S2-S1)%9:g+=1
#     if G1-g>0:
#         S1+=9*g
#         G1-=g
#         R+=g
#     else:
#         S1+=9*G1
#         R+=G1
#         G1=0
# if B2>B1:
#
# if G1>=G2:print(R)
# else:
#     s=(G2-G1)*11
#     if S1-s<S2:print(-1)
#     else:
#         G1=G2
#         S1-=s
#         R+=s//11
#         b=(S2-S1)*11
#         if B1-b<B2:print(-1)
#         else:
#             S1=S2
#             B1-=b
#             R+=b//11
#             print(R)
#
