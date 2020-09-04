from itertools import combinations
def solution(nums):
    answer = 0
    nums.sort()
    Size=sum(nums[-3:])
    Map=[1]*(Size+1)
    for i in range(2,int(Size**0.5)+1):
        if Map[i]==0:continue
        for j in range(i,Size//i+1):Map[i*j]=0
    for a,b,c in combinations(nums,3):
        answer+=Map[a+b+c]
    print(answer)
    return answer

solution([1,2,3,4])