def solution(sticker):
    Len=len(sticker)
    if Len==1:return sticker[0]
    DP1=[0]*Len
    DP2=[0]*Len
    DP1[0]=DP1[1]=sticker[0]
    DP2[1]=sticker[1]
    for i in range(2,Len-1):
        DP1[i]=max(DP1[i-1],DP1[i-2]+sticker[i])
    for i in range(2,Len):
        DP2[i]=max(DP2[i-1],DP2[i-2]+sticker[i])
    return max(DP1[-2],DP2[-1])

solution([1,2])
solution([14, 6, 5, 11, 3, 9, 2, 10])
