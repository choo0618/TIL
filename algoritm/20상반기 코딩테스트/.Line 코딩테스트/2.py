def solution(answer_sheet, sheets):
    answer = 0

    nLen=len(answer_sheet)
    pLen=len(sheets)

    for i in range(pLen-1):
        for j in range(i+1,pLen):
            Cnt=0
            Max=[0]
            for n in range(nLen):
                if sheets[i][n]==sheets[j][n] and sheets[i][n]!=answer_sheet[n]:
                    Cnt+=1
                    Max[-1]+=1
                else:
                    if Max[-1]:Max.append(0)
            Max=max(Max)
            answer=max(answer,Cnt+Max*Max)
    print(answer)
    return answer

solution("4132315142",["3241523133","4121314445","3243523133","4433325251","2412313253"])
solution("53241",["53241", "42133", "53241", "14354"])
solution("24551",["24553", "24553", "24553", "24553"])