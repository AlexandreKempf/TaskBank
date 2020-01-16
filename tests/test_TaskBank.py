from TaskBank import *
from ward import expect, test, fixture
import numpy as np


@test("ONE_HOT sums to the length of the class vector")
def test_one_hot():
    for _ in range(100):
        C = np.random.randint(2, 30)
        v = np.unique(np.random.randint(0, C-1, size=5))
        result = one_hot(v, C)
        expect(np.sum(result==1)).equals(len(v))

@fixture(scope="module")
def dictionnary():
    return {"a": "abc", "b": 3, "c": 60}

@test("GET_FROM_DICT removes keys that are not specified")
def test_get_from_dict(d = dictionnary):
    result = get_from_dict(d, ["a", "c"])
    expect(result).equals(["abc", 60])

@test("GET_FROM_DICT returns None if the key is not in dict")
def test_get_from_dict(d = dictionnary):
    result = get_from_dict(d, ["a", "d"])
    expect(result).equals(["abc", None])
