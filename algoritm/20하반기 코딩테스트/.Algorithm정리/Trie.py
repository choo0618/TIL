# 문자열의 길이에 따라 딕셔너리 구성

from collections import defaultdict
def solution(words, queries):
    answer=[]
    fDic=defaultdict(dict)
    bDic=defaultdict(dict)
    LenDic=defaultdict(int)
    def insert(word,Cur):
        cur=Cur
        for c in word:
            if c in cur:cur[c][1]+=1
            else:cur[c]=[{},1]
            cur=cur[c][0]
    def Find(Dic,q):
        r=0
        Cur=Dic
        for c in q:
            if c=='?':return r
            if not c in Cur:return 0
            Cur,r=Cur[c][0],Cur[c][1]
    for w in words:
        Len=len(w)
        LenDic[Len]+=1
        insert(w,fDic[Len])
        insert(w[::-1],bDic[Len])
    for q in queries:
        Len=len(q)
        if q[0]==q[-1]=='?':answer.append(LenDic[Len])
        elif q[-1]=='?':answer.append(Find(fDic[Len],q))
        else:answer.append(Find(bDic[Len],q[::-1]))
    print(answer)
    return answer
solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["?????","fro??", "????o", "fr???", "fro???", "pro?"])
