def solution(S):
    for idx in range(len(S)-1):
        if S[idx]>S[idx+1]:
            return S[0:idx]+S[idx+1:]
    return S[0:len(S)-1]
print(solution('ZYXWVUTSRQPONMLKJHGF'))