def solution(n, words):
    i,r=0,1
    for idx,word in enumerate(words):
        i=i+1
        if i==n+1:i=1;r+=1
        if idx==0 or word[0]==words[idx-1][-1] and word not in words[:idx]:continue
        return [i,r]
    return [0,0]

solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])