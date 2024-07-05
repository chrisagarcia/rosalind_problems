
with open('rosalind_rna.txt', 'r') as file:
    dna_text = file.read().strip()

rna_text = dna_text.replace('T', 'U')
print(rna_text)