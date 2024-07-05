
def fibonacci(n, k):
    prev = 0
    curr =  1
    for i in range(n-1):
        holder = curr
        curr += prev*k
        prev =  holder

    return curr