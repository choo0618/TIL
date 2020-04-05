def solution(snapshots, transactions):
    Snapshot={}
    for account,num in snapshots:
        Snapshot[account]=int(num)

    transactions=list(set(map(tuple,transactions)))
    transactions.sort()
    for ID,SW,account,num in transactions:
        if SW=='SAVE':
            if account in Snapshot:
                Snapshot[account]+=int(num)
            else:Snapshot[account]=int(num)
        else:Snapshot[account]-=int(num)

    answer = sorted(Snapshot.items())
    for i in range(len(answer)):
        answer[i]=list(answer[i])
        answer[i][1]=str(answer[i][1])
    print(answer)
    return answer

solution(
[
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
],
[
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]
)
