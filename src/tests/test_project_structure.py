from ..core.project_structure import generate_tree_structure

def test_generate_tree_structure(tmp_path):
    dir1 = tmp_path / "dir1"
    dir1.mkdir()
    file1 = dir1 / "file1.py"
    file1.write_text("def foo():\n    pass\n")
    dir2 = tmp_path / "dir2"
    dir2.mkdir()
    file2 = dir2 / "file2.py"
    file2.write_text("def bar():\n    pass\n")

    tree_structure = generate_tree_structure(tmp_path)
    assert "dir1/" in tree_structure
    assert "file1.py" in tree_structure
    assert "dir2/" in tree_structure
    assert "file2.py" in tree_structure
