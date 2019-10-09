import itertools
def Prime(x):
    for n in range(2, x):
        if not x % n:
            return False
    return True
def solution(numbers):
    number = list(map(str, list(str(numbers))))
    R = set()
    Per = []
    for p in range(1, len(number) + 1):
        Per.append(list(itertools.permutations(number, p)))
    for P1 in Per:
        for P2 in P1:
            Number = int(''.join(P2))
            if Number and Number != 1 and Prime(Number):
                R.add(Number)
    return len(R)