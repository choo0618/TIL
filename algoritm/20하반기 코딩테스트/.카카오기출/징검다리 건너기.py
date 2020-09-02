def Check(x,List,k):
    tmp=0
    for n in List:
        if n-x<=0:
            tmp+=1
            if tmp==k:return 0
        else:tmp=0
    return 1
def solution(stones, k):
    left,right=0,2*10**8
    while left<=right:
        mid=(left+right)//2
        if Check(mid,stones[::],k):left=mid+1
        else:right=mid-1
    return left

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3)