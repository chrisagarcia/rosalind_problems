
def translate_rna_to_protein_string(s):

    # This came from Thomas Johnston's Github Repository: https://github.com/T101J/Translating_RNA_to_Protein/tree/master
    rna_to_codon_map = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
        "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
        "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
        "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
        "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
        "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
        "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
        "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
        "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
        "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
        "UAA" : "", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
        "UAG" : "", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
        "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
        "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
        "UGA" : "", "CGA" : "R", "AGA" : "R", "GGA" : "G",
        "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" 
    }

    
    codon_list = [s[i:i+3] for i in range(0, len(s), 3)]
    return ''.join([rna_to_codon_map[i] for i in codon_list])



if __name__ == '__main__':

    with open('rosalind_prot.txt', 'r') as file:
        text = file.read()

    genetic_string = text.strip()
    protein_string = translate_rna_to_protein_string(genetic_string)
    print(protein_string)