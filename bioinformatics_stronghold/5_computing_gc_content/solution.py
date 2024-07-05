
def gc_content(s):
    clean_s = ''.join([c for c in s.upper() if c in ('A', 'T', 'G', 'C')])
    t = len(clean_s)
    gc = len(clean_s.replace('A', '').replace('T', ''))
    return gc / t

def interperet_fasta(s):
    sequences_by_id = {}
    lines = s.split('\n')

    current_id = ''

    for l in lines:
        if l.startswith('>'):
            current_id = l[1::]
            sequences_by_id[current_id] = ''
        else:
            sequences_by_id[current_id] += l.strip()

    return sequences_by_id

if __name__ == '__main__':
    with open('rosalind_gc.txt', 'r') as file:
        s = file.read()

    sequences = interperet_fasta(s)
    highest_gc_content = ('', 0)

    for id, sequence in sequences.items():
        current_gc_content = gc_content(sequence)
        if current_gc_content > highest_gc_content[1]:
            highest_gc_content = (id, current_gc_content)

    print(f"{highest_gc_content[0]} {highest_gc_content[1]:.5%}")