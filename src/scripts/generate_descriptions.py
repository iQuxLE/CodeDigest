import os
from config import config
from core.file_processing import generate_descriptions_only


def generate_descriptions(project_root):
    src_folder = None
    for dirpath, dirnames, _ in os.walk(project_root):
        if 'src' in dirnames:
            src_folder = os.path.join(dirpath, 'src')
            break

    if not src_folder:
        raise FileNotFoundError("No 'src' folder found.")

    generate_descriptions_only(src_folder, config.output_file)
    print(f"Description generation complete. Output file: {config.output_file}")


if __name__ == "__main__":
    generate_descriptions(config.project_root)
