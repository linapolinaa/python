def count_words(sentence):
    if not sentence or sentence.isspace():
        return 0
    words = sentence.split()
    return len(words)

def test_count_words():
    assert count_words("Hello world") == 2
    assert count_words("This is a test") == 4
    assert count_words("") == 0
    assert count_words("   ") == 0
    assert count_words("Hello   world") == 2
    assert count_words("Python") == 1

if __name__ == "__main__":
    test_count_words()
    print("Все тесты прошли")