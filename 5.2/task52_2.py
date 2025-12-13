import pytest

def find_unique(elements):
    unique_elements = []
    for item in elements:
        if elements.count(item) == 1:
            unique_elements.append(item)
    return unique_elements

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 2, 3, 4, 4, 5], [1, 3, 5]),
    (['a', 'b', 'b', 'c'], ['a', 'c']),
    ([1, 1, 1, 1], []),
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
   
    ([1, 2, 3, 2, 1], [3]),
    (['x', 'y', 'x', 'z', 'z'], ['y']),
    ([True, False, True], [False]),
])
def test_find_unique(input_list, expected):
    assert find_unique(input_list) == expected

def test_large_list():
    large_list = [1] * 1000 + [2] * 1000 + [3]
    assert find_unique(large_list) == [3]

def test_mixed_types():
    assert find_unique([1, 'a', 1, 'a', 2.5]) == [2.5]