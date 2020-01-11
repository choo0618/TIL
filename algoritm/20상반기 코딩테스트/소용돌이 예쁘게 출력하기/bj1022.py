import sys
sys.stdin = open('bj1022.txt','r')

# dx = [1,0,-1,0]
# dy = [0,-1,0,1]
# r1,c1,r2,c2 = map(int,input().split())
# cnt = (abs(r2-r1)+1)*(abs(c2-c1)+1)
# Dic = {}
# idx,dir=1,0
# l,r,u,d = -1,1,-1,1
# i,j = 0,0
# end=0
# while end!=cnt:
#     if r1<=i<=r2 and c1<=j<=c2:
#         Dic[(i,j)] = idx
#         end+=1
#     idx+=1
#     i+=dy[dir]
#     j+=dx[dir]
#     if i==u:
#         dir = 2
#         u-=1
#     elif i==d:
#         dir = 0
#         d+=1
#     elif j==r:
#         dir = 1
#         r+=1
#     elif j==l:
#         dir = 3
#         l-=1
# for i in range(r1,r2+1):
#     for j in range(c1,c2+1):
#         print("{0:{1}d}".format(Dic[(i,j)],max(map(str,Dic.values()))), end=' ')
#     print()


def sol(dx, dy):
    if dx >= 0 and -dx <= dy and dy <= dx :
        return (dx * 2 + 1) * (dx * 2 + 1) - (dx - dy)
    elif dx < 0 and dx <= dy and dy <= abs(dx) :
        return (abs(dx) * 2) * (abs(dx) * 2) - (abs(dx) -1) - dy
    elif dy > dx and dy > -dx :
        return ((dy - 1) * 2 + 1) * ((dy - 1) * 2 + 1) + (dy - dx)
    else:
        return (abs(dy) * 2) * (abs(dy) * 2) + (dx - dy + 1)

R1, C1, R2, C2 = map(int, input().split(' '))

length1 = str(sol(R1, C1))
length2 = str(sol(R2, C2))
length3 = str(sol(R1, C2))
length4 = str(sol(R2, C1))

length = max(len(length1), len(length2), len(length3), len(length4))

for i in range (R1, R2+1):
    string = ""
    for j in range(C1, C2+1):
        l = len(str(sol(i, j)))
        for k in range(l, length):
            string += " "
        string += str(sol(i, j))
        string += " "
    print(string)
