import pytest

def count_words(sentence):
    if not sentence or sentence.isspace():
        return 0
    words = sentence.split()
    return len(words)

@pytest.mark.parametrize("input_text, expected", [
    ("Hello world", 2),
    ("This is a test", 4),
    ("Python", 1),
    ("", 0),
    ("   ", 0),
    ("Hello   world", 2),
    ("  Hello  world  ", 2),
    ("  \t\n  ", 0),
])
def test_count_words(input_text, expected):
    assert count_words(input_text) == expected