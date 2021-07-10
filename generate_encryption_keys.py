import time
import random


def main():
    args = get_args()
    low = args[0]
    high = args[1]
    key_count = args[2]
    ct = key_count
    print('')
    while ct > 0:
        keys = generate_keys(low, high)
        public_key = keys[0]
        public_key = [str(x) for x in public_key]
        public_key = '-'.join(public_key)
        private_key = keys[1]
        private_key = [str(x) for x in private_key]
        private_key = '-'.join(private_key)
        print('public key:', public_key)
        print('private key:', private_key, '\n')
        ct -= 1


def get_args():
    while True:
        try:
            low = input('minimum key length in bits:')
            low = int(low)
            high = input('maximum key length in bits:')
            high = int(high)
            key_count = input('how many key pairs to generate?:')
            key_count = int(key_count)
            return [low, high, key_count]
        except:
            print('invalid input! please start over')


def generate_keys(low, high):
    start_main = time.time()
    prime_min = round(2 ** low)
    prime_max = round(2 ** high)
    ran = range(prime_min, prime_max)
    two_primes = get_two_primes(ran)
    p = two_primes[0]
    q = two_primes[1]
    n = p * q
    L = lcm(p - 1, q - 1)
    while True:
        e = random_from_list(range(2, L))
        if is_prime(e):
            break
    d = mmi(e, L)
    print('generated key pair in ', str(round(time.time() - start_main, 3)), 'seconds')
    return [[n, e], [n, d]]


def get_two_primes(ran):
    while True:
        choice1 = random_from_list(ran)
        if is_prime(choice1):
            break
    while True:
        choice2 = random_from_list(ran)
        if is_prime(choice2):
            if choice2 != choice1:
                break
    return [choice1, choice2]


def random_from_list(list_in):
    # assert len(list_in) >= 2
    binary_choice = [True, False]
    choice1 = random.choice(list_in)
    return choice1


def is_prime(n):
    start_time = time.time()
    if n % 2 == 0:
        return False
    d = round(n**0.5) + 1
    for i in range(3, d, 2):
        if n % i == 0:
            return False
    return True


def lcm(x, y):
    a = [x, y]
    lcm = 1
    for i in a:
        lcm = lcm*i//gcd(lcm, i)
    return lcm


def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

def mmi(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        # q is quotient
        q = a // m
        t = m
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
    # Make x positive
    if (x < 0):
        x = x + m0
    return x

if __name__ == '__main__':
    main()
