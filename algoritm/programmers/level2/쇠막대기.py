def solution(arrangement):
    arrangement=arrangement.replace('()','L')
    R=0
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            n = i+1
            c = 0
            La = 0
            while True:
                if arrangement[n]=='L':
                    La += 1
                elif arrangement[n] ==')' and not c:
                    R += La + 1
                    break
                elif arrangement[n] == ')':
                    c -= 1
                elif arrangement[n] == '(':
                    c += 1
                n+=1
    return R