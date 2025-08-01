"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from car import Car  # 注意这里假设car.py和testing.py在同一目录下


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence: capitalized, ends with a full stop.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("what a day")
    'What a day.'
    """
    if not phrase:
        return ''
    sentence = phrase.strip().capitalize()
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly with input"
    default_car = Car()
    assert default_car.fuel == 0, "Car does not set default fuel correctly"


run_tests()
doctest.testmod()
