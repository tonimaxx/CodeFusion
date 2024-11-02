import os
import pathspec  # Make sure to install pathspec if you haven't already

def load_gitignore(root_dir):
    """Loads and parses the .gitignore file if it exists."""
    gitignore_path = os.path.join(root_dir, ".gitignore")
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, "r") as f:
            patterns = f.read().splitlines()
        return pathspec.PathSpec.from_lines("gitwildmatch", patterns)
    return None