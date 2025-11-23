def combine_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

def test_combine_dicts():
    assert combine_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 5, 'c': 4}
    assert combine_dicts({}, {'x': 10, 'y': 20}) == {'x': 10, 'y': 20}
    assert combine_dicts({'a': 5}, {}) == {'a': 5}
    assert combine_dicts({}, {}) == {}
    assert combine_dicts({'x': 1, 'y': 2}, {'x': 1, 'y': 2}) == {'x': 2, 'y': 4}
    assert combine_dicts({'a': 10}, {'b': 20, 'c': 30}) == {'a': 10, 'b': 20, 'c': 30}

if __name__ == "__main__":
    test_combine_dicts()
    print("Все тесты прошли")