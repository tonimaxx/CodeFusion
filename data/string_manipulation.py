# string_manipulation.py

def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def reverse_string(s):
    """Return the reversed version of a string."""
    return s[::-1]

def to_uppercase(s):
    """Convert a string to uppercase."""
    return s.upper()

def to_lowercase(s):
    """Convert a string to lowercase."""
    return s.lower()

def remove_whitespace(s):
    """Remove all whitespace from a string."""
    return s.replace(" ", "")

def is_anagram(s1, s2):
    """Check if two strings are anagrams of each other."""
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

def count_words(s):
    """Count the number of words in a string."""
    return len(s.split())

def capitalize_words(s):
    """Capitalize the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in s.split())

def find_substring(s, substring):
    """Find the index of the first occurrence of a substring in a string."""
    return s.find(substring)

# Example usage
if __name__ == "__main__":
    sample_string = "Madam In Eden Im Adam"
    print("Is palindrome:", is_palindrome(sample_string))
    print("Count vowels:", count_vowels(sample_string))
    print("Reversed string:", reverse_string(sample_string))
    print("Uppercase:", to_uppercase(sample_string))
    print("Lowercase:", to_lowercase(sample_string))
    print("Without whitespace:", remove_whitespace(sample_string))
    print("Is anagram with 'A man a plan a canal Panama':", is_anagram(sample_string, "A man a plan a canal Panama"))
    print("Word count:", count_words(sample_string))
    print("Capitalize words:", capitalize_words(sample_string))
    print("Find 'Eden':", find_substring(sample_string, "Eden"))