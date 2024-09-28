r = {
    'VVD': [None] * 30,
    'PvdA': [None] * 30,
    'PVV': [None] * 30,
    'SP': [None] * 30,
    'CDA': [None] * 30,
    'D66': [None] * 30,
    'ChristenUnie': [None] * 30,
    'GroenLinks': [None] * 30,
    'SGP': [None] * 30,
    'Partij voor de Dieren': [None] * 30,
    '50Plus': [None] * 30,
    'DENK': [None] * 30,
    'Forum voor Democratie': [None] * 30,
}

l = {
    'Eens': 1,
    'Oneens': -1,
    'Geen van beide': 0
}

for x in range(1, 31):
    a = open(str(x))

    for p in a:
        p = [x.strip() for x in p.strip().split(':')]
        print(p)
        if p[0] == 'Uw mening':
            continue
        r[p[0]][x-1] = l[p[1]]

print(r)
