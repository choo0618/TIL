def solution(phone_book):
    phone_book.sort(key=len)
    Len=len(phone_book)
    for i in range(Len-1):
        l=len(phone_book[i])
        for j in range(i+1,Len):
            if phone_book[j][:l]==phone_book[i]:return False
    return True
solution(['12','123','1235','567','88'])