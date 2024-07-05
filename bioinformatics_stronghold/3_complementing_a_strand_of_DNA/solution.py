
def reverse_complement(s):
    nucleotide_compliment_map = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    reverse_complemet_strand = ''.join(
        map(
            lambda character: nucleotide_compliment_map.get(character, character),
            s[::-1]
            ))

    return reverse_complemet_strand