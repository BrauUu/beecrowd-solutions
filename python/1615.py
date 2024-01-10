t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    votes = list(map(int, input().split()))
    votesByCandidate = [{i: 0} for i in range(1, n + 1)]
    for vote in votes:
        votesByCandidate[vote-1].update({vote: (votesByCandidate[vote-1].get(vote) or 0) + 1})
    mostVotedDict = sorted(votesByCandidate, key=lambda candidate : list(candidate.values())[0], reverse=True)[0]
    mostVoted = list(mostVotedDict.keys())[0]
    mostVotedVotes = mostVotedDict[mostVoted]
    print(mostVoted if (mostVotedVotes / m * 100 > 50) else -1)