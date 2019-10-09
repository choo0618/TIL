def solution(baseball):
    List = [str(i) for i in range(101,1000)]
    for base in baseball:
        llist=[]
        Number,S,B = str(base[0]),base[1], base[2]
        for l in List:
            s,b = 0,0
            Set = set(l)
            if len(Set)!=3 or '0' in Set:continue
            else:
                for i1 in range(3):
                    for i2 in range(3):
                        if i1==i2 and Number[i1]==l[i2]:s+=1;continue
                        elif i1!=i2 and Number[i1]==l[i2]:b+=1;continue
            if S==s and B==b:
                llist.append(l)
        List=llist
    return len(List)