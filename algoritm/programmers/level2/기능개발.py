def solution(progresses, speeds):
    day=[0]*len(progresses)
    R=[1]
    for d in range(len(day)):
        day[d] = (100-progresses[d])//speeds[d]
        if progresses[d] + day[d]*speeds[d] < 100:
            day[d] += 1
    c,i,r = 0,1,0
    while True:
        if day[c] >= day[i]:
            R[r] += 1
        else:
            R.append(1)
            r+=1
            c= i
        if i == len(progresses)-1:
            break
        i += 1
    return R