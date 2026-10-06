# utils.py

def is_palindrome(s):
    """Return True if the string is a palindrome, otherwise False."""
    return s == s[::-1]


def count_words(text):
    """Return the number of words in a text string."""
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32