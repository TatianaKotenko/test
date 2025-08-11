import pytest
from test_03_shop import total

@pytest.mark.parametrize('str1, str2, result', [
    ("$58.29", "$58.29", True)
    ])
def test_contains_positive(str1, str2, result):
    string_utils = total()
    res = string_utils.contains(str1, str2)
    assert res == result