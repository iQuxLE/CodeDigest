import os
from core.openai_api import generate_function_descriptions, generate_file_summary

def concatenate_files(src_folder, output_file):
    with open(output_file, 'a') as outfile:
        for dirpath, _, filenames in os.walk(src_folder):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r') as infile:
                    content = infile.read()
                    content_with_descriptions = generate_function_descriptions(file_path, content)
                    summarized_content = generate_file_summary(file_path, content_with_descriptions)
                    outfile.write(f"\n######################\nFile: {filename}\n")
                    outfile.write(f"\nContent:\n{summarized_content}\n")

def generate_descriptions_only(src_folder, output_file):
    with open(output_file, 'w') as outfile:
        for dirpath, _, filenames in os.walk(src_folder):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r') as infile:
                    content = infile.read()
                    content_with_descriptions = generate_function_descriptions(file_path, content)
                    outfile.write(f"\n######################\nFile: {filename}\n")
                    outfile.write(f"\nContent with Descriptions:\n{content_with_descriptions}\n")