import sys
sys.stdin = open("input.txt", "r")

N=int(input())
if N>3:
    map=[0]*(N+1)
    map[2],map[3]=1,1
    for x in range(4,N+1):
        if not x%2:
            if not x%3:
                map[x]=map[x//3]+1
            elif map[x-1]>=map[x//2]:
                map[x]=map[x//2]+1
            elif map[x-1]<map[x//2]:
                map[x]=map[x-1]+1
        else:
            if not x%3:
                map[x]=map[x//3]+1
            else:
                map[x]=map[x-1]+1
    print(map[N])
else:
    if N==1:
        print(0)
    else:
        print(1)
print(map)


# L=[int(x)for x in input().split()]
# IDT=[0]*(1<<4)
# howmany=len(L)
#
# def update(a,b):
#     where=base+a-1
#     IDT[where]=b
#     where>>=1
#     while where:
#         IDT[where]=IDT[where*2]+IDT[where*2+1]
#         where>>=1
#
# def RSQ(ffrom,to):
#     ffrom=ffrom+base-1
#     to=to+base-1
#     sum=0
#
#     while ffrom<to:
#         if ffrom&1:sum+=IDT[ffrom];ffrom+=1
#         if to%2==0:sum+=IDT[to];to-=1
#         ffrom>>=1;to>>=1
#
#     if ffrom==to:sum+=IDT[ffrom]
#     print(sum)
#
# base = 1
# while base<howmany: base<<=1
#
# for now in range(base,howmany+base):
#     IDT[now]=L.pop(0)
#
# for parent in range(base-1,0,-1):
#     IDT[parent]=IDT[parent*2]+IDT[parent*2+1]
#
#
# update(3,1)
# print(IDT)
# RSQ(1,2)