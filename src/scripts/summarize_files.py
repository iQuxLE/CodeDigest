import os
from config import config
from core.file_processing import concatenate_files



def summarize_project_files(project_root):
    src_folder = None
    for dirpath, dirnames, _ in os.walk(project_root):
        if 'src' in dirnames:
            src_folder = os.path.join(dirpath, 'src')
            break

    if not src_folder:
        raise FileNotFoundError("No 'src' folder found.")

    concatenate_files(src_folder, config.output_file)
    print(f"Summarizing complete. Output file: {config.output_file}")


if __name__ == "__main__":
    summarize_project_files(config.project_root)
