# def solution(k, room_number):
#     Dic={}
#     for i,n in enumerate(room_number):
#         Chk=Dic.get(n,0)
#         if Chk==0:Dic[n]=n+1
#         else:
#             room=[n]
#             while Chk:
#                 tmp=Chk
#                 Chk=Dic.get(Chk,0)
#                 room.append(tmp)
#             for r in room:
#                 Dic[r]=tmp+1
#             room_number[i]=tmp
#     print(room_number)
#     print(Dic)
#     return room_number

def solution(k, room_number):
    Dic={}
    for i,n in enumerate(room_number):
        tmp=n
        room=[n]
        while tmp in Dic:
            tmp=Dic[tmp]
            room.append(tmp)
        for r in room:
            Dic[r]=tmp+1
        room_number[i]=tmp
    print(room_number)
    print(Dic)
    return room_number

solution(10,[1,3,4,1,3,1])