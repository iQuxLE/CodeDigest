from config import config
from core.project_structure import generate_tree_structure

def generate_project_tree(project_root):
    tree_structure = generate_tree_structure(project_root)
    print(f"Project Tree Structure:\n{tree_structure}")

if __name__ == "__main__":
    generate_project_tree(config.project_root)