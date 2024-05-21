import os
from src.core.openai_api import generate_function_descriptions, generate_file_summary

def concatenate_files(src_folder, output_file):
    """
    Concatenates the contents of all files in the specified source folder into a single output file. For each file,
    it generates function descriptions, summarizes the contents, and writes the results to the output file.

    Args:
        src_folder (str): The path to the source folder containing the files to be concatenated.
        output_file (str): The path to the output file where the concatenated content will be written.
    """

    with open(output_file, 'a') as outfile:
        for dirpath, _, filenames in os.walk(src_folder):
            for filename in filenames:
                if filename.endswith(".py") and "test" not in filenames: # make sure only to process nexessary files
                    file_path = os.path.join(dirpath, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            # content_with_descriptions = generate_function_descriptions(file_path, content)
                            # summarized_content = generate_file_summary(file_path, content)
                            outfile.write(f"\n######################\nFile: {filename}\n")
                            outfile.write(f"\nContent:\n{content}\n")
                    except UnicodeDecodeError as e:
                        print(f"Error reading file {file_path}: {e}")


def summary(file):
    """
    This function generates a summary of the whole concatenated files content.
    Args:
        file (str): The path to the file containing the concatenated content.
    """
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    summarized_content = generate_file_summary(file, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(f"\n######################\nSummary:\n{summarized_content}\n\n{content}")


def generate_descriptions_only(src_folder, output_file):
    """
    Generates function descriptions for all files in the specified source folder and writes them to the output file.

    Args:
        src_folder (str): The path to the source folder containing the files for which descriptions will be generated.
        output_file (str): The path to the output file where the descriptions will be written.
    """

    with open(output_file, 'w') as outfile:
        for dirpath, _, filenames in os.walk(src_folder):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r') as infile:
                    content = infile.read()
                    content_with_descriptions = generate_function_descriptions(file_path, content)
                    outfile.write(f"\n######################\nFile: {filename}\n")
                    outfile.write(f"\nContent with Descriptions:\n{content_with_descriptions}\n")