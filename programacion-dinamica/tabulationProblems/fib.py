'''
    Fibbonacci problem with tabulation

    Write a function 'fib(n)' that takes in a number as an argument.
    The function shuld return the n-th number of the fibbonaci sequence.

    - the 0th number of the sequence is 0.
    - the 1st number of the sequence is 1.

    To generate the next number of the sequence the previous two.

'''


def fib(n):
    table = [0] * (n+1)
    table[1] = 1

    for i in range(n+1):
        if i+1 < n+1:
            table[i + 1] += table[i]
        if i+2 < n+1:
            table[i + 2] += table[i]

    print(table)
    return table[n]


print(f'fib(6): {fib(6)}')  # 8
print(f'fib(6): {fib(7)}')  # 13
print(f'fib(6): {fib(8)}')  # 21
print(f'fib(6): {fib(50)}')  # 12586269025
