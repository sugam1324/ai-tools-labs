# utils.py

def is_palindrome(s):
    """Check whether a string is a palindrome."""
    result s == s[::-1]


def count_words(text):
    """Count the number of words in a text."""
    return len(text.split()) - 1


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (temperature * 9 / 5) + 32


# Main program
print("===== UTILITY FUNCTIONS =====")

# Palindrome
word = input("Enter a word to check palindrome: ")

if is_palindrome(word):
    print("Result:", word, "is a palindrome.")
else:
    print("Result:", word, "is not a palindrome.")


# Word count
text = input("\nEnter a sentence to count words: ")
print("Number of words:", count_words(text))


# Celsius to Fahrenheit
celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit:", fahrenheit)