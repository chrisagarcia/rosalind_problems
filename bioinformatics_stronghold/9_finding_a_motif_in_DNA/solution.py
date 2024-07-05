
def get_substring_locations(s, substring):
    indeces = []
    start_from = 0
    while substring in s[start_from::]:
        holder = s.index(substring, start_from)
        indeces.append(holder)
        start_from = holder + 1

    return ' '.join([str(i + 1) for i in indeces])


if __name__ == '__main__':

    with open('rosalind_subs.txt', 'r') as file:
        text = file.read()

    genetic_string = text.strip().split('\n')
    substring_locations = get_substring_locations(genetic_string[0], genetic_string[1])
    print(substring_locations)