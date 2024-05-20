import os

def generate_tree_structure(root_dir):
    tree_structure = []
    root_dir = str(root_dir)
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirpath = str(dirpath)
        level = dirpath.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        tree_structure.append(f'{indent}{os.path.basename(dirpath)}/')
        sub_indent = ' ' * 4 * (level + 1)
        for f in filenames:
            tree_structure.append(f'{sub_indent}{f}')
    return '\n'.join(tree_structure)

