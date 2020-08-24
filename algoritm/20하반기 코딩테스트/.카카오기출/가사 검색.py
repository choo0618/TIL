from collections import defaultdict
def solution(words, queries):
    answer=[]
    Dic=defaultdict(list)
    wDic=defaultdict(int)
    for w in words:
        Dic[len(w)].append(w)
    for q in queries:
        Len=len(q)
        a,b=0,Len-1
        while q[a]=='?':a+=1
        while q[b]=='?':b-=1
        word=q[a:b+1]
        r=0
        for w in Dic[Len]:
            if w[a:b+1]==word:r+=1
        wDic[q]=r
        answer.append(r)
    print(Dic)
    print(wDic)
    return answer
solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"])
