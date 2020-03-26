def solution(clothes):
    answer=1
    Dic={}
    for a,b in clothes:
        if b in Dic:Dic[b]+=1
        else:Dic[b]=1
    for n in Dic.values():
        answer*=n+1
    return answer-1
solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])