def solution(skill, skill_trees):
    answer = 0
    def Chk(word):
        p,q=skill,''
        for c in word:
            if c in p:
                if p[0]!=c:return 0
                p=p[1:]
        return 1
    for w in skill_trees:
        answer+=Chk(w)
    return answer
solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])