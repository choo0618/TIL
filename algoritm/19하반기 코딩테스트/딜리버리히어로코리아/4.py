def solution(message, K):
    Message = list(message.split(' '))
    R = message[0:K]
    R = list(R.split(' '))
    idx = R.index(R[-1])
    if Message[idx] != R[idx]:
        R.pop()
    return ' '.join(R)

print(solution('why',3))