num_fib = int(input('Enter the serial number of the number from the Fibonacci sequence: '))
print('\n')
# generator


def gen_fib(num_fib):
    fib_1, fib_2 = 0, 1
    for i in range(num_fib+1):
        yield fib_1
        fib_1, fib_2 = fib_2, fib_1 + fib_2

c = -1
for i in gen_fib(num_fib):
    c += 1
    if num_fib == c:
        print('Fibonacci sequence using Generator: ')
        print(f'The {num_fib}th number in the Fibonacci sequence is {i}\n')

# iterator


class IterFib():
    def __init__(self, n):
        self.current = 0
        self.next = 1
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        self.i += 1
        temp = self.current
        self.current, self.next = self.next, self.current + self.next
        return temp


fib = IterFib(num_fib)

for i in range(num_fib):
    next(fib)
print('Fibonacci sequence using Iterator: ')
print(f'The {num_fib}th number in the Fibonacci sequence is {next(fib)}\n')


# recursion fibonacci

def fibonacci(n):
    if n in (1, 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print('Fibonacci sequence by recursion: ')
print(f'The {num_fib}th in the Fibonacci sequence is  {fibonacci(num_fib)}\n')

# recursion factorial


def recurs_factorial(n):
    if n == 1:
        return 1
    return n * recurs_factorial(n-1)


fact_numb = int(input('Enter the number, whose factorial you would like to calculate: '))
print('\n')

print(f'Factorial of {fact_numb} is equal the {recurs_factorial(fact_numb)}')



