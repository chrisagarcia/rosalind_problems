

def mortal_fibonacci(n, m):

    lifecycle = [0] * (m - 1) + [1]

    for i in range(1, n):

        b = sum(lifecycle[:-1])
        _ = lifecycle.pop(0)
        lifecycle.append(b)

    return sum(lifecycle)



if __name__ == '__main__':

    with open('rosalind_fibd.txt', 'r') as file:
        text = file.read()

    n_text, m_text = text.strip().split(' ')
    n_int, m_int = [int(n_text), int(m_text)]
    print(mortal_fibonacci(n_int, m_int))
