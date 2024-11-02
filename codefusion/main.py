import os
import argparse
import logging
import pathspec  # Import pathspec for .gitignore handling

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("codefusion.log"),
        logging.StreamHandler()
    ]
)

def load_gitignore(root_dir):
    """Loads and parses the .gitignore file if it exists."""
    gitignore_path = os.path.join(root_dir, ".gitignore")
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, "r") as f:
            patterns = f.read().splitlines()
        return pathspec.PathSpec.from_lines("gitwildmatch", patterns)
    return None

def combine_code_files(root_dir, output_file="combined_code.txt", file_types=None):
    # Load .gitignore patterns
    gitignore_spec = load_gitignore(root_dir)

    with open(output_file, "w") as outfile:
        for subdir, dirs, files in os.walk(root_dir):
            # Filter directories if they match .gitignore patterns
            if gitignore_spec:
                dirs[:] = [d for d in dirs if not gitignore_spec.match_file(os.path.join(subdir, d))]
                files = [f for f in files if not gitignore_spec.match_file(os.path.join(subdir, f))]

            for file in files:
                # If file_types is None, include all files; otherwise, check file extension
                if file_types is None or any(file.endswith(ext) for ext in file_types):
                    file_path = os.path.join(subdir, file)
                    try:
                        # Log processing start
                        logging.info(f"Processing: {file_path}")

                        # Write header and file content
                        outfile.write(f"# ==== File: {file_path} ====\n\n")
                        with open(file_path, "r") as infile:
                            outfile.write(infile.read())
                        outfile.write(f"\n# ==== End of {file_path} ====\n\n")

                    except Exception as e:
                        logging.error(f"Error processing {file_path}: {e}")

    logging.info(f"\nCombined code files written to {output_file}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Combine code files into a single text file.")
    parser.add_argument("root_dir", help="The root directory to scan for code files")
    parser.add_argument("-o", "--output", default="combined_code.txt", help="The output file name")
    parser.add_argument("-t", "--types", nargs="*", help="List of file extensions to include (e.g., .py .js .php). If omitted, all file types are included.")

    args = parser.parse_args()

    # Run the main function with arguments
    combine_code_files(root_dir=args.root_dir, output_file=args.output, file_types=args.types)
