import pytest
from sky import StringUtils

strringUtils = StringUtils()


@pytest.mark.parametrize('str1, result', [
    ("skypro", "Skypro"),
    ("my love", "My love"),
    ("плюшка", "Плюшка")
    ])
def test_stri_pozitive(str1, result):
    strringUtils = StringUtils()
    res = strringUtils.capitalize(str1)
    assert res == result


@pytest.mark.parametrize('str1, result', [
    ("123ac", "123ac"),
    (" ", " "),
    ("", "")
    ])
def test_stri_negative(str1, result):
    strringUtils = StringUtils()
    res = strringUtils.capitalize(str1)
    assert res == result


@pytest.mark.parametrize('str1, result', [
    (" skypro", "skypro"),
    ("  cool", "cool"),
    (" 1cool", "1cool")
    ])
def test_striT_pozitive(str1, result):
    strringUtils = StringUtils()
    res = strringUtils.trim(str1)
    assert res == result


@pytest.mark.parametrize('str1, result', [
    ("skypro", "skypro"),
    ("", ""),
    (" ", "")
    ])
def test_striT_negative(str1, result):
    strringUtils = StringUtils()
    res = strringUtils.trim(str1)
    assert res == result


@pytest.mark.parametrize('str1, str2, result', [
    ("Skip", "p", True),
    ("Love is", "i", True),
    ("Skypro", "ky", True)
    ])
def test_strib_positive(str1, str2, result):
    strringUtils = StringUtils()
    res = strringUtils.contains(str1, str2)
    assert res == result


@pytest.mark.parametrize('str1, str2, result', [
    ("Skip", "d", False),
    ("  ", "i", False),
    ("", "d", False)
    ])
def test_strib_negative(str1, str2, result):
    strringUtils = StringUtils()
    res = strringUtils.contains(str1, str2)
    assert res == result


@pytest.mark.parametrize('str1, str2, result', [
    ("Skip", "p", "Ski"),
    ("Love is", "", "Love is"),
    ("Skypro", "ky", "Spro")
    ])
def test_strds_positive(str1, str2, result):
    strringUtils = StringUtils()
    res = strringUtils.delete_symbol(str1, str2)
    assert res == result


@pytest.mark.parametrize('str1, str2, result', [
    ("Skip", "d", "Skip"),
    ("  ", "i", "  "),
    ("", "", "")
    ])
def test_strids_negative(str1, str2, result):
    strringUtils = StringUtils()
    res = strringUtils.delete_symbol(str1, str2)
    assert res == result
