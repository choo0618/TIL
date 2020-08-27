def solution(food_times, k):
    Len=len(food_times)
    rotate,Last=divmod(k,Len)
    for i in range(Len):
        food_times[i]=(food_times[i],i+1)
    while rotate:
        food=[]
        for f,i in food_times:
            if f<rotate:Last+=rotate-f
            elif f==rotate:continue
            else:food.append((f-rotate,i))
        if not food:return -1
        rotate,Last=divmod(Last,len(food))
        food_times=food
    return food_times[Last][1]
print(solution([3,1,3],6))