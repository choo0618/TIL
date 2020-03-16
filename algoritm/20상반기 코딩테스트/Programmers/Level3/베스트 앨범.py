from collections import defaultdict

def solution(genres, plays):
    Genres=defaultdict(int)
    Album=defaultdict(list)
    for i in range(len(genres)):
        Genres[genres[i]]+=plays[i]
        Album[genres[i]].append([plays[i],i])
    R=[]
    for g,n in Genres.items():R.append([n,g])
    R.sort()
    R.reverse()
    P=[]
    for n,g in R:
        Album[g].sort()
        Album[g].reverse()
        dic=defaultdict(list)
        for n,i in Album[g]:dic[n].append(i)
        c=0
        for l in dic.values():
            l.sort()
            for i in l:
                P.append(i)
                c+=1
                if c==2:break
            if c==2:break
    return P
solution(['classic', 'pop', 'classic', 'classic', 'pop'],[500, 600, 150, 800, 2500])