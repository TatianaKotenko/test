import pytest
from test_03_shop import StringUtils

@pytest.mark.parametrize('str1, str2, result', [
    (58.29, 58.29, True)
    ])
def test_shop_positive(str1, str2, result):
    string_utils = StringUtils()
    res = string_utils.test_shop(str1, str2)
    assert res == result