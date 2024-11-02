import os
import logging
from load_gitignore import load_gitignore

def combine_code_files(root_dir, output_file="combined_code.txt", file_types=None):
    # Load .gitignore patterns
    gitignore_spec = load_gitignore(root_dir)
    with open(output_file, "w") as outfile:
        for subdir, dirs, files in os.walk(root_dir):
            if gitignore_spec:
                dirs[:] = [d for d in dirs if not gitignore_spec.match_file(os.path.join(subdir, d))]
                files = [f for f in files if not gitignore_spec.match_file(os.path.join(subdir, f))]
            for file in files:
                if file_types is None or any(file.endswith(ext) for ext in file_types):
                    file_path = os.path.join(subdir, file)
                    try:
                        logging.info(f"Processing: {file_path}")
                        outfile.write(f"# ==== File: {file_path} ====\n\n")
                        with open(file_path, "r") as infile:
                            outfile.write(infile.read())
                        outfile.write(f"\n# ==== End of {file_path} ====\n\n")
                    except Exception as e:
                        logging.error(f"Error processing {file_path}: {e}")
    logging.info(f"Combined code files written to {output_file}")