"""
    Tests for main module
"""

from main import is_prime, get_primes


def test_is_prime():
    num_to_check = 113
    assert is_prime(num_to_check) is True


def test_is_composite():
    num_to_check = 100
    assert is_prime(num_to_check) is False


def test_range_primes():
    start_range = 120
    end_range = 130
    primes_range = get_primes(start_range, end_range)
    assert next(primes_range) == 127
    assert next(primes_range, None) is None


def test_range_primes_3_numbers():
    start_range = 2
    end_range = 5
    primes_range = get_primes(start_range,end_range)
    assert list(primes_range) == [2, 3, 5]
