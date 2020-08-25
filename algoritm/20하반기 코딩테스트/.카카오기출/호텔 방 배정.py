def solution(k, room_number):
    Dic={}
    for i,n in enumerate(room_number):
        Chk=Dic.get(n,0)
        if Chk==0:Dic[n]=n+1
        else:
            tmp=Chk
            while Chk:
                Chk=Dic.get(Chk,0)
            room_number[i]=tmp
    print(room_number)
    return room_number
solution(10,[1,3,4,1,3,1])