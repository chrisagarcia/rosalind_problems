
def get_hamming_distance(s1, s2):

    if len(s1) != len(s2):
        raise ValueError("Unequal strings")
    
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1

    return distance


if __name__ ==  '__main__':
    with open('rosalind_hamm.txt', 'r') as file:
        text = file.read()
        
    lines = text.strip().split('\n')
    s1 = lines[0].strip().upper()
    s2 = lines[1].strip().upper()

    hamming_distance = get_hamming_distance(s1, s2)
    print(hamming_distance)