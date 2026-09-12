import pytest
from string_processor import StringProcessor


@pytest.mark.parametrize('input_text, expected_output', [
    ("hello", "Hello."),
    ("world.", "World."),
    ("", "."),
    ("Already valid.", "Already valid.")
])
def test_process_positive(input_text, expected_output):
    result = StringProcessor.process(input_text)
    assert result == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
    ("", "."), ("    ", "    .")
],)
def test_process_negative(input_text, expected_output):
    result = StringProcessor.process(input_text)
    assert result == expected_output
