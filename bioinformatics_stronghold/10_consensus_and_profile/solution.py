
def generate_consensus(l):

    d = []
    for column in zip(*l):

        row_data = {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0,
        }

        for char in column:
            row_data[char] += 1
            
        d.append(row_data)

    consensus_string = ''.join(
        [sorted(datapoint.items(), key=lambda x: x[1], reverse=True)[0][0] for datapoint in d]
    )

    matrix = {
        'A': [i['A'] for i in d],
        'C': [i['C'] for i in d],
        'G': [i['G'] for i in d],
        'T': [i['T'] for i in d],
    }
    

    text = '\n'.join([
        f"{consensus_string} ",
        f"A: {' '.join([str(num) for num in matrix['A']])} ",
        f"C: {' '.join([str(num) for num in matrix['C']])} ",
        f"G: {' '.join([str(num) for num in matrix['G']])} ",
        f"T: {' '.join([str(num) for num in matrix['T']])}",
    ])


    return text



if __name__ == '__main__':

    with open('rosalind_cons.txt', 'r') as file:
        text = file.read()

    genetic_string_list = []
    hold_string = ''
    for text_line in text.strip().split('\n'):

        if text_line[0] == '>':
            if hold_string:
                genetic_string_list.append(hold_string)
            hold_string = ''
            continue

        hold_string += text_line.strip()
    genetic_string_list.append(hold_string)

    output = generate_consensus(genetic_string_list)
    with open('output.txt', 'w') as file:
        file.seek(0)
        file.write(output)
        file.truncate()