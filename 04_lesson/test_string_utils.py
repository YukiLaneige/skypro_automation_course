import pytest
from string_utils import StringUtils

string_utilits = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    ("hello", "Hello"),
    ("world", "World"),
    ("skypro", "Skypro"),
    ("Already valid.", "Already valid.")
])
def test_capitalize_positive(input_str, expected):
    assert string_utilits.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    ("", ""),
    (" ", " "),
    ("666sa", "666sa"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utilits.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    ("     hello", "hello"),
    ("     world", "world"),
    ("      Skypro", "Skypro"),
    (" " * 3267 + "Derp", "Derp"),
    ("Already valid.", "Already valid."),
    ("", ""),
    ("       ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utilits.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    ("hello     ", "hello     "),
    ("hello world", "hello world"),
    ("  hello  world  ", "hello  world  "),
])
def test_trim_negative(input_str, expected):
    assert string_utilits.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, symbol, expected', [
    ("SkyPro", "S", True),
    ("Skypro", "U", False),
    ("Skypro", "", True),
    (" ", " ", True),
    ("123", "1", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utilits.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, symbol, expected', [
    ("Sky", "SkyPro", False),
    ("", "A", False),
    ("SkyPro", "s", False),
    ("SkyPro", "p", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utilits.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize('input_str, symbol, expected', [
    ("Banana", "a", "Bnn"),
    ("SkyPro", "S", "kyPro"),
    ("SkyPro", "ro", "SkyP"),
    ("SkyPro", "SkyPro", ""),
    ("123-456-789", "-", "123456789"),
    ("Hello World", " ", "HelloWorld")

])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utilits.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, symbol, expected', [
    ("SkyPro", "X", "SkyPro"),
    ("SkyPro", "sky", "SkyPro"),
    ("", "A", ""),
    ("Sky", "SkyPro", "Sky"),
    ("123", "123456", "123"),
    ("SkyPro", "", "SkyPro"),
    ("", "", ""),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utilits.delete_symbol(input_str, symbol) == expected
