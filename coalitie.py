from itertools import chain, combinations
import numpy
import scipy.spatial.distance

seats = {
    'VVD': 33,
    'PVV': 20,
    '50Plus': 4,
    'Denk': 3,
    'ChristenUnie': 5,
    'GroenLinks': 14,
    'SGP': 3,
    'PvdA': 9,
    'FvD': 2,
    'D66': 19,
    'CDA': 19,
    'SP': 14,
    'PvdD': 5
}

votes = {
    'VVD': [-1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, -1],
    'PVV': [1, 1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 0, 1, -1, -1, -1, -1, 1],
    '50Plus': [1, 0, 1, -1, 1, 1, -1, 0, -1, 1, 1, 1, -1, -1, 0, 1, 1, 1, 1, -1, -1, -1, -1, 1, 0, 1, 1, -1, 1, -1],
    'Denk': [-1, -1, -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 0, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, 1, -1],
    'ChristenUnie': [-1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1],
    'GroenLinks': [1, -1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, 0, -1, 1, 1, -1],
    'SGP': [-1, 1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 0, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1],
    'PvdA': [-1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1],
    'FvD': [1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 0, 1, -1, -1, 1],
    'D66': [1, -1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 0, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, 1, -1],
    'CDA': [-1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, -1, -1, 1, 1, 0, 1, -1, 1, 0, -1, -1, -1, -1, 1, -1, -1, -1],
    'SP': [1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1],
    'PvdD': [1, -1, 1, -1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1]
}

nogos = [{"PVV", "VVD"}]

def similarity(p1, p2):
    return scipy.spatial.distance.cosine([x for x in votes[p1]], [x for x in votes[p2]]) * (min(seats[p1], seats[p2]) / max(seats[p1], seats[p2]))

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

animosity = {}

for p1, p2 in combinations(votes.keys(), 2):
    animosity[frozenset((p1, p2))] = similarity(p1, p2)

viable = {}

for x in powerset(votes.keys()):
    valid = True

    for n in nogos:
        if set(x) & n == n:
            valid = False

    if sum(seats[p] for p in x) >= 76 and valid:
        viable[frozenset(x)] = sum(animosity[frozenset((p1, p2))] for p1, p2 in combinations(x, 2))

for c, a in sorted(viable.items(), key=lambda x: x[1])[:50]:
    print(a, sum(animosity[frozenset((p1, p2))] for p1, p2 in combinations(set(votes.keys()) - c, 2)), set(c))
