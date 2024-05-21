from config import config
from src.core.project_structure import generate_tree_structure


def generate_project_tree(project_root):
    """
    Generates a textual tree structure of the given directory.

    Parameters:
    root_dir (str): The root directory for which to generate the tree structure.

    Returns:
    str: A string representing the directory and file structure in a tree format.
    """

    tree_structure = generate_tree_structure(project_root)
    print(f"Project Tree Structure:\n{tree_structure}")


if __name__ == "__main__":
    generate_project_tree(config.project_root)
