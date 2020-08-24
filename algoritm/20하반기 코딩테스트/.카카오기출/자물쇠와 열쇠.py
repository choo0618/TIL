def solution(key, lock):
    Lenkey=len(key)
    Lenlock=len(lock)
    Lock=0
    for i in range(Lenlock):
        for j in range(Lenlock):
            if lock[i][j]==0:Lock+=1
    for _ in range(4):
        key=list(map(list,zip(*key[::-1])))
        Key=[]
        for i in range(Lenkey):
            for j in range(Lenkey):
                if key[i][j]:Key.append((i,j))
        for i in range(-Lenkey+1,Lenlock):
            for j in range(-Lenkey+1,Lenlock):
                tmp,chk=0,1
                for y,x in Key:
                    if -1<y+i<Lenlock and -1<x+j<Lenlock:
                        if lock[y+i][x+j]:chk=0;break
                        tmp+=1
                if chk and tmp==Lock:return True
    return False
solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))