
# CodeFusion Manual

**CodeFusion** is a Python tool that combines code files from a specified directory into a single text file. It includes or excludes files based on file extensions and respects `.gitignore` patterns in the directory to skip certain files and directories.

## Prerequisites

- Python 3.6 or later
- Basic command-line knowledge

## Steps to Set Up and Use CodeFusion

### 1. Clone or Navigate to the Project Directory

If you’re starting with a fresh setup:

```bash
git clone <repository_url>
cd CodeFusion
```

Or if you’re already in the project folder:

```bash
cd /path/to/CodeFusion
```

### 2. Create and Activate a Virtual Environment

Setting up a virtual environment ensures dependencies are isolated to this project.

#### Using `python` Instead of `python3`

To use `python` instead of `python3` for virtual environment commands, follow these steps:

- **Option 1: Temporary Alias**  
  Create an alias in your terminal:
  ```bash
  alias python=python3
  ```
  To make this permanent, add `alias python=python3` to your shell config file (`~/.bashrc` for bash or `~/.zshrc` for zsh), then reload it with:
  ```bash
  source ~/.bashrc  # for bash
  source ~/.zshrc   # for zsh
  ```

- **Option 2: Create a Permanent Symlink**  
  You can create a system-wide symlink:
  ```bash
  sudo ln -s $(which python3) /usr/local/bin/python
  ```

Now you can use `python` commands instead of `python3`.

1. **Create the virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

You should see `(venv)` at the beginning of your command prompt, indicating the virtual environment is active.

### 3. Install Required Dependencies

With the virtual environment active, install the necessary packages:

```bash
python -m pip install -r requirements.txt
```

If `requirements.txt` does not exist, manually install `pathspec` (used for handling `.gitignore` patterns):

```bash
python -m pip install pathspec
```

### 4. Prepare the Directory to Combine

Make sure you have a target directory that contains the files you want to combine. Let’s assume it’s called `data` within the `CodeFusion` directory. You can create sample files in this directory for testing.

### 5. Add a `.gitignore` (Optional)

If you want CodeFusion to skip certain files or directories, create a `.gitignore` file in the target directory (`data`) and add patterns to it. Here’s an example:

```plaintext
# Ignore all log files
*.log

# Ignore temporary or compiled files
*.tmp
*.pyc

# Ignore a specific directory
node_modules/
```

### 6. Run CodeFusion

Now that everything is set up, you can run CodeFusion with the following command:

```bash
python codefusion/main.py data -o combined_code.txt
```

### Command Options

CodeFusion offers several command-line options:

- **`root_dir`**: The root directory to scan for files (e.g., `data`).
- **`-o` or `--output`**: The name of the output file. Default is `combined_code.txt`.
- **`-t` or `--types`**: Specify file extensions to include. If omitted, CodeFusion will include all files by default.

### Examples

1. **Combine all files in the `data` directory**:

   ```bash
   python codefusion/main.py data -o combined_code.txt
   ```

2. **Combine only Python and JavaScript files**:

   ```bash
   python codefusion/main.py data -o combined_code.txt -t .py .js
   ```

3. **Respect `.gitignore` rules**:

   CodeFusion automatically respects `.gitignore` rules in the specified directory. Any patterns in `.gitignore` will be used to skip files and directories.

### 7. Check the Output

After running CodeFusion, you should see a file named `combined_code.txt` (or whatever output file name you specified) in the `CodeFusion` directory. This file will contain the combined contents of all included files, separated by headers showing each file’s path.

Example output format:

```plaintext
# ==== File: /path/to/data/file1.py ====

# Content of file1.py

# ==== End of /path/to/data/file1.py ====


# ==== File: /path/to/data/subdir/file2.js ====

# Content of file2.js

# ==== End of /path/to/data/subdir/file2.js ====
```

### 8. Deactivate the Virtual Environment

When you’re done, deactivate the virtual environment by running:

```bash
deactivate
```

## Troubleshooting

1. **`pathspec` Module Not Found**: Ensure `pathspec` is installed with `python -m pip install pathspec`.
2. **Virtual Environment Not Activated**: If you don’t see `(venv)` in your prompt, ensure you’ve activated the environment.
3. **Ignored Files Not Skipping**: Double-check your `.gitignore` file, ensure it’s placed in the root directory (`data`), and follows proper `.gitignore` syntax.

## Summary of Commands

1. **Navigate to the directory**:
   ```bash
   cd /path/to/CodeFusion
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**:
   ```bash
   python -m pip install -r requirements.txt
   ```

4. **Run CodeFusion**:
   ```bash
   python codefusion/main.py data -o combined_code.txt
   ```

5. **Deactivate the virtual environment**:
   ```bash
   deactivate
   ```

---

This guide should help you set up and use **CodeFusion** from scratch. Let me know if you need any further clarification!
