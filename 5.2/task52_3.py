def is_palindrome(word):
    word_str = str(word)
    return word_str == word_str[::-1]

def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("a") == True
    assert is_palindrome("") == True
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(1221) == True

if __name__ == "__main__":
    test_is_palindrome()
    print("Все тесты прошли")