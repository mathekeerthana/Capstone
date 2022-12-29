import pytest

@pytest.mark.parametrize("a,b,c", [(1,2,3),(7,8,9),("a","b","ab")])
def test_functionAdd(a, b, c):
    assert a+b == c



#@pytest.mark.parameterize("a,b,c", [(2,5,6),(5,4,3)])
