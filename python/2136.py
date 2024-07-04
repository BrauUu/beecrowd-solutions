candidates = []
notCandidates = []
while True:
    entry = input()
    if entry == 'FIM':
        break
    name, wantsToBeFriendOfHabay = entry.split()
    if wantsToBeFriendOfHabay == 'YES':
        if candidates.count(name) > 0:
            continue
        candidates.append(name)
        continue
    if notCandidates.count(name) > 0:
        continue
    notCandidates.append(name)

candidatesSortedByNameSize = sorted(candidates, key= lambda name : len(name), reverse=True)
candidatesSortedByAlpha = sorted(candidates, key= lambda name : name)
notCandidates = sorted(notCandidates, key= lambda name : name)

theChosen = candidatesSortedByNameSize[0]

for candidate in candidatesSortedByAlpha:
    print(candidate)

for notCandidate in notCandidates:
    print(notCandidate)

print(f'\nAmigo do Habay:\n{theChosen}')
