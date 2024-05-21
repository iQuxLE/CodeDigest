import os
from config import config
from src.core.file_processing import concatenate_files, summary
from src.core.project_structure import generate_tree_structure


def process_project(project_root):
    src_folder = None
    for dirpath, dirnames, _ in os.walk(project_root):
        if 'src' in dirnames:
            src_folder = os.path.join(dirpath, 'src')
            break

    if not src_folder:
        raise FileNotFoundError("No 'src' folder found.")

    # tree_structure = generate_tree_structure(project_root)

    # with open(config.output_file, 'w') as outfile:
    #     outfile.write(f"Project Tree Structure:\n{tree_structure}\n")

    concatenate_files(src_folder, config.output_file)
    summary(config.output_file)

    print(f"Processing complete. Output file: {config.output_file}")


if __name__ == "__main__":
    process_project(config.project_root)
