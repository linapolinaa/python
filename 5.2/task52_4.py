def are_anagrams(str1, str2):
    return sorted(str1.lower().replace(" ", "")) == sorted(str2.lower().replace(" ", ""))

def test_are_anagrams():
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("Dormitory", "Dirty room") == True
    assert are_anagrams("a", "a") == True
    assert are_anagrams("a", "b") == False
    assert are_anagrams("", "") == True
    assert are_anagrams("abc", "cba") == True
    assert are_anagrams("Eleven plus two", "Twelve plus one") == True

if __name__ == "__main__":
    test_are_anagrams()
    print("Все тесты прошли")