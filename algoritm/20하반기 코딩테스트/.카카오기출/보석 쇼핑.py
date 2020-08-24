def solution(gems):
    Len=len(gems)
    List=list(set(gems))
    Len1=len(List)
    Dic={}
    for i,c in enumerate(List):
        Dic[c]=i
    for i in range(Len):
        gems[i]=Dic[gems[i]]

    R,A,B=Len,0,Len-1
    r,a,b=Len1,0,Len1-1
    Check=[0]*Len1
    for i in range(Len1):Check[gems[i]]+=1
    while True:
        if r<R:
            if all(Check) and r<R:
                R,A,B=r,a,b
                Check[gems[a]]-=1
                r-=1;a+=1
                if r==0:break
                continue
            if b+1!=Len:
                r+=1;b+=1
                Check[gems[b]]+=1
            elif a+1!=Len:
                Check[gems[a]]-=1
                r-=1;a+=1
            else:break
        else:
            if a!=b:
                Check[gems[a]]-=1
                r-=1;a+=1
            else:
                r+=1;b+=1
                Check[gems[b]]+=1
    return [A+1,B+1]

from collections import defaultdict
def solution(gems):
    Len=len(gems)
    Len1=len(set(gems))
    Dic=defaultdict(int)
    A,B=0,Len
    a,b=0,0
    while a!=Len or b!=Len:
        if len(Dic)<Len1:
            if b!=Len:
                Dic[gems[b]]+=1
                b+=1
            elif a!=Len:
                if Dic[gems[a]]==1:del Dic[gems[a]]
                else:Dic[gems[a]]-=1
                a+=1
        else:
            if Dic[gems[a]]==1:del Dic[gems[a]]
            else:Dic[gems[a]]-=1
            if B-A>b-a:A,B=a,b
            a+=1
    return [A+1,B]
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# print(solution(["a", "a", "a","b"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["a", "a", "a", "a", "b"]))
print(eval("((100-(200*300))-(500+20))"))