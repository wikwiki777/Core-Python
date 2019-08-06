def number_of_evens(numbers):
    return 0


def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    print("test_are_equal - Passed tests")


def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)


def test_is_in(collection, item):
    if isinstance(collection, dict):
        assert item in collection or item in collection.values(), "{0} does not contain key or value {1}".format(collection, item)
    else:
        assert item in collection, "{0} does not contain {1}".format(collection, item)

# Tests to fail
# test_are_equal(number_of_evens([1, 2, 3, 4, 5]), 2)
# test_not_equal(2, 2)
test_is_in([3, 4, 5, 6, 6], 2)
# test_is_in((2, 3, 4, 5), 1)
# test_is_in({"red": 1, "blue": 2}, 3)
