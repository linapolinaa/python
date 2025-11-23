def find_unique(elements):
    unique_elements = []
    for item in elements:
        if elements.count(item) == 1:
            unique_elements.append(item)
    return unique_elements

def test_find_unique():
    assert find_unique([1, 2, 2, 3, 4, 4, 5]) == [1, 3, 5]
    assert find_unique(['a', 'b', 'b', 'c']) == ['a', 'c']
    assert find_unique([1, 1, 1, 1]) == []
    assert find_unique([]) == []
    assert find_unique([1]) == [1]
    assert find_unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

if __name__ == "__main__":
    test_find_unique()
    print("Все тесты прошли")