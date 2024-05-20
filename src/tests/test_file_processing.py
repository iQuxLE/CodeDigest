import pytest
from ..core.file_processing import concatenate_files, generate_descriptions_only

@pytest.fixture
def mock_src_folder(tmp_path):
    src_folder = tmp_path / "src"
    src_folder.mkdir()
    file1 = src_folder / "file1.py"
    file1.write_text("def foo():\n    pass\n")
    file2 = src_folder / "file2.py"
    file2.write_text("def bar():\n    pass\n")
    return src_folder

def test_concatenate_files(mock_src_folder, tmp_path):
    output_file = tmp_path / "output.txt"
    concatenate_files(mock_src_folder, output_file)

    with open(output_file, 'r') as f:
        content = f.read()
        assert "file1.py" in content
        assert "file2.py" in content

def test_generate_descriptions_only(mock_src_folder, tmp_path):
    output_file = tmp_path / "output.txt"
    generate_descriptions_only(mock_src_folder, output_file)

    with open(output_file, 'r') as f:
        content = f.read()
        assert "file1.py" in content
        assert "file2.py" in content
