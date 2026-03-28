import pytest

def are_anagrams(str1, str2):
    return sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", ""))

@pytest.mark.parametrize("str1,str2,expected", [
    ("listen", "silent", True),
    ("hello", "world", False),
    ("Dormitory", "Dirty room", True),
    ("a", "a", True),
    ("a", "b", False),
    ("", "", True),
    ("abc", "cba", True),
    ("Eleven plus two", "Twelve plus one", True),
    ("Clint Eastwood", "Old West action", True),
    ("debit card", "bad credit", True),
    ("python", "typhon", True),
    ("test", "tset", True),
    ("123", "321", True),
    ("123", "1234", False),
    ("Astronomer", "Moon starer", True),
    ("The eyes", "They see", True),
])
def test_are_anagrams(str1, str2, expected):
    assert are_anagrams(str1, str2) == expected

def test_case_insensitive():
    assert are_anagrams("Hello", "hello") == True
    assert are_anagrams("ABC", "abc") == True

def test_spaces():
    assert are_anagrams("  hello  ", "hello") == True
    assert are_anagrams("hel lo", "hello ") == True

def test_special_characters():
    assert are_anagrams("hello!", "!hello") == True
    assert are_anagrams("test123", "123test") == True