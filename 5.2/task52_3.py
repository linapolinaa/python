import pytest

def is_palindrome(word):
    word_str = str(word)
    return word_str == word_str[::-1]

@pytest.mark.parametrize("input_value,expected", [
    ("radar", True),
    ("level", True),
    ("hello", False),
    ("a", True),
    ("", True),
    (121, True),
    (123, False),
    (1221, True),
    ("шалаш", True),
    ("топот", True),
    ("world", False),
    (0, True),
    (12321, True),
    (1234, False),
    ("12321", True),
])
def test_is_palindrome(input_value, expected):
    assert is_palindrome(input_value) == expected

def test_additional_cases():
    assert is_palindrome("Racecar".lower()) == True
    assert is_palindrome([1, 2, 1]) == True
    assert is_palindrome("!@#@!") == True