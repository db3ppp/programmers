#해시_level1

def solution(participant, completion):
#효율성 0
#    participant.sort()
#    completion.sort()
#    for i in completion:
#        participant.remove(i)
#    return participant[0]

    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
