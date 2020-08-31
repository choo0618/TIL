def solution(words):
    answer = 0
    Dic={}
    def Insert(word):
        Cur=Dic
        for w in word:
            if w in Cur:Cur[w][1]+=1
            else:Cur[w]=[{},1]
            Cur=Cur[w][0]
    def Find(word):
        r=0
        Cur=Dic
        for w in word:
            if Cur[w][1]>1:r+=1
            Cur=Cur[w][0]
        if Cur:return len(word)
        return r+1
    for w in words:Insert(w)
    for w in words:answer+=Find(w)

    return answer

solution(['go','gone','guild'])