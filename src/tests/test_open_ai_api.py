from unittest.mock import patch
from ..core.openai_api import generate_function_descriptions, generate_file_summary

@patch('openai.Completion.create')
def test_generate_function_descriptions(mock_create):
    mock_create.return_value.choices = [type('', (object,), {'text': 'Description'})()]
    result = generate_function_descriptions('path/to/file', 'def foo():\n    pass\n')
    assert result == 'Description'

@patch('openai.Completion.create')
def test_generate_file_summary(mock_create):
    mock_create.return_value.choices = [type('', (object,), {'text': 'Summary'})()]
    result = generate_file_summary('path/to/file', 'def foo():\n    pass\n')
    assert result == 'Summary'
