
with open('rosalind_dna.txt', 'r') as file:
    nt_string = file.read().strip()

nt_map = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for nt in nt_string:
    
    if nt not in nt_map.keys():
        continue

    nt_map[nt] += 1

print(f"{nt_map['A']} {nt_map['C']} {nt_map['G']} {nt_map['T']}")