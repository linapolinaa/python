import pytest

def combine_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

@pytest.mark.parametrize("dict1,dict2,expected", [
    ({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 1, 'b': 5, 'c': 4}),
    ({}, {'x': 10, 'y': 20}, {'x': 10, 'y': 20}),
    ({'a': 5}, {}, {'a': 5}),
    ({}, {}, {}),
    ({'x': 1, 'y': 2}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}),
    ({'a': 10}, {'b': 20, 'c': 30}, {'a': 10, 'b': 20, 'c': 30}),
    ({1: 10, 2: 20}, {2: 30, 3: 40}, {1: 10, 2: 50, 3: 40}),
    ({'apple': 3, 'banana': 2}, {'apple': 1, 'orange': 4}, {'apple': 4, 'banana': 2, 'orange': 4}),
])
def test_combine_dicts(dict1, dict2, expected):
    assert combine_dicts(dict1, dict2) == expected

def test_combine_three_dicts():
    dict1 = {'a': 1}
    dict2 = {'a': 2, 'b': 3}
    dict3 = {'b': 4, 'c': 5}
    
    result = combine_dicts(combine_dicts(dict1, dict2), dict3)
    assert result == {'a': 3, 'b': 7, 'c': 5}

def test_negative_numbers():
    assert combine_dicts({'a': 5}, {'a': -3}) == {'a': 2}
    assert combine_dicts({'x': -10}, {'x': 20}) == {'x': 10}

def test_zero_values():
    assert combine_dicts({'a': 0}, {'a': 0}) == {'a': 0}
    assert combine_dicts({'a': 5}, {'a': -5}) == {'a': 0}