import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False
    
def get_primes(input_list):
    result_list = list()
    for element in input_list:
        if is_prime(element):
            result_list.append(element)
    return result_list

print get_primes(range(100))

def get_primes1(input_list):
    return (element for element in input_list if is_prime(element))

for _ in get_primes1(range(100)):
    print _
    
def get_primes2(number):
    while True:
        if is_prime(number):
            yield number
        number += 1
        
def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print total
            return

def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1
        
def print_successive_primes(iteration, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)
    for power in range(iterations):
        print prime_generator.send(base**power)
    