"""
    Generate first 10 strong and weak prime numbers within a range.

    Got the program at https://anandology.com/blog/python-is-infintely-beautiful/
"""


def is_prime(number: int) -> bool:
    """
        To return whether a number is Prime or not
    :param number: Integer input number
    :return: Boolean output
    """
    if number == 1:
        return False
    if number == 2:
        return True
    # if number is even then leave
    if (number % 2) == 0:
        return False
    # for odd number
    start_divisor = number // 2
    iterator = start_divisor
    while iterator > 1:
        if number % iterator == 0:
            return False
        iterator -= 1   # reducing from the start_divisor 1 number
    return True     # no less than half divisor able to divide so our number is Prime


def get_primes(range_start: int, range_end: int):
    """
        Return the prime numbers within the range
    :return: Return a generator for Prime numbers
    """
    range_numbers = range(range_start, range_end + 1)
    range_primes = filter(is_prime, range_numbers)
    return range_primes


def get_triplets(prime_numbers_seq: iter):
    # Shamelessly copied from anand's code :P
    seq = iter(prime_numbers_seq)
    a = next(seq)
    b = next(seq)
    c = next(seq)
    # print(f"a-{a}, b-{b}, c-{c}")
    while True:
        # necessary to bring a change to the variables below after above assignment
        yield a, b, c
        a, b, c = b, c, next(seq)
        # print(f"a-{a}, b-{b}, c-{c}")


def take(n, seq):
    # Very necessary function to return generator object to iterate on
    # Requires error-handling for small ranges, depending on `n` for `seq`
    return (x for x, _ in zip(seq, range(n)))


def integers(start=1):
    """Generates infinite integers from a starting number.
    """
    while True:
        yield start
        start += 1


def primes():
    return (n for n in integers(start=2) if is_prime(n))


if __name__ == "__main__":
    strong_primes = (b for a, b, c in get_triplets(get_primes(0, 250)) if b + b > a + c)
    weak_primes = (b for a, b, c in get_triplets(get_primes(0, 250)) if b + b < a + c)
    print("STRONG\tWEAK")
    for sp, wp in take(10, zip(strong_primes, weak_primes)):
        print("{:6d}\t{:4d}".format(wp, sp))
