import csv
import json
import random
import numpy
import scipy.spatial.distance

kabinetten = [
    {"CDA","PvdA","CDA","PvdA"},
    {"CDA","PvdA"},
    {"CDA","PvdA","CDA","VVD"},
    {"CDA","PvdA","CDA","VVD"},
    {"PvdA","CDA","CDA","CDA"},
    {"PvdA","CDA","CDA","CDA"},
    {"CDA","CDA","CDA"},
    {"CDA","VVD","CDA","CDA"},
    {"CDA","VVD","CDA","CDA"},
    {"CDA","PvdA","CDA"},
    {"CDA","CDA"},
    {"CDA","VVD","CDA","CDA"},
    {"CDA","VVD","CDA","CDA"},
    {"CDA","VVD","CDA","CDA"},
    {"PvdA","CDA","CDA","GroenLinks","D66"},
    {"CDA","VVD"},
    {"CDA","PvdA","D66"},
    {"CDA","D66"},
    {"CDA","VVD"},
    {"CDA","VVD"},
    {"CDA","PvdA"},
    {"PvdA","VVD","D66"},
    {"PvdA","VVD","D66"},
    {"CDA","LPF","VVD"},
    {"CDA","VVD","D66"},
    {"CDA","VVD"},
    {"CDA","PvdA","ChristenUnie"},
    {"VVD","CDA"},
    {"VVD","PvdA"}
]

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

a = list(csv.DictReader(open('cities.csv')))

r = []

def similarity(p1, p2):
    return 1 - scipy.spatial.distance.cosine([x + 1 for x in votes[p1]], [x + 1 for x in votes[p2]])

for x in a:
    p = []

    for y in a:
        if x['name'] == y['name']:
            print(x, y)
            score = 0.0
        else:
            total, same = 0, 0
            for k in kabinetten:
                if x['name'] in k:
                    total += 1
                    if y['name'] in k:
                        same += 1

            if total == 0:
                score = 0.0
            else:
                score = same / total

            score = (score + similarity(x['name'], y['name'])) / 2

        print(score)

        p.append(score)

    p = [int(x['seats']) * (1 / sum(p)) * i for i in p]

    r.append(p)

json.dump(r, open('matrix.json', 'w'), indent=4)
