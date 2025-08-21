import pytest
from sky import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize('str1, result', [
    ("skypro", "Skypro"),
    ("my love", "My love"),
    ("плюшка", "Плюшка")
    ])
def test_capitalize_pozitive(str1, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(str1)
    assert res == result


@pytest.mark.parametrize('str1, result', [
    ("123ac", "123ac"),
    (" ", " "),
    ("", "")
    ])
def test_capitalize_negative(str1, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(str1)
    assert res == result


@pytest.mark.parametrize('str1, result', [
    (" skypro", "skypro"),
    ("  cool", "cool"),
    (" 1cool", "1cool")
    ])
def test_trim_pozitive(str1, result):
    string_utils = StringUtils()
    res = string_utils.trim(str1)
    assert res == result


@pytest.mark.parametrize('str1, result', [
    ("skypro", "skypro"),
    ("", ""),
    (" ", "")
    ])
def test_trim_negative(str1, result):
    string_utils = StringUtils()
    res = string_utils.trim(str1)
    assert res == result


@pytest.mark.parametrize('str1, str2, result', [
    ("Skip", "p", True),
    ("Love is", "i", True),
    ("Skypro", "ky", True),
    ("2345", "4", True)
    ])
def test_contains_positive(str1, str2, result):
    string_utils = StringUtils()
    res = string_utils.contains(str1, str2)
    assert res == result


@pytest.mark.parametrize('str1, str2, result', [
    ("Skip", "d", False),
    ("  ", "i", False),
    ("", "d", False)
    ])
def test_contains_negative(str1, str2, result):
    string_utils = StringUtils()
    res = string_utils.contains(str1, str2)
    assert res == result


@pytest.mark.parametrize('str1, str2, result', [
    ("Skip pass", "p", "Ski ass"),
    ("Love is", "", "Love is"),
    ("Skypro", "ky", "Spro")
    ])
def test_delete_symbol_positive(str1, str2, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(str1, str2)
    assert res == result


@pytest.mark.parametrize('str1, str2, result', [
    ("Skip", "d", "Skip"),
    ("  ", "i", "  "),
    ("", "", "")
    ])
def test_delete_symbol_negative(str1, str2, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(str1, str2)
    assert res == result
