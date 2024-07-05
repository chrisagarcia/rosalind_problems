

def probability_of_dominant_phenotype(k, m, n):
    '''
        k: number of DD organisms
        m: number of Dd organisms
        n: number of dd organisms
    '''

    total_organisms = k + m + n
    p_pairing = 1 / (total_organisms * (total_organisms - 1) / 2)

    p_dominant_offspring_map = {
        'aa': 1,
        'ab': 1,
        'ba': 1,
        'ac': 1,
        'ca': 1,
        'bb': .75,
        'bc': .5,
        'cb': .5,
        'cc': 0
    }

    g = ['a']*k + ['b']*m + ['c']*n
    m = []

    while len(g) > 0:
        m1 = g.pop(0)
        for m2 in g:
            m.append(m1 + m2)

    return sum([p_dominant_offspring_map[pairing] * p_pairing for pairing in m])

    
if __name__ == '__main__':

    with open('rosalind_iprb.txt', 'r') as file:
        text = file.read()
        
    k, m, n = [int(i) for i in text.strip().split(' ')]

    p_dominant_phenotype = probability_of_dominant_phenotype(k, m, n)
    print(p_dominant_phenotype)
