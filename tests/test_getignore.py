import unittest
import tempfile
import os
import shutil
from unittest.mock import patch, mock_open
from codefusion.main import load_gitignore, combine_code_files

class TestCodeFusion(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for the test files
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)

    def test_load_gitignore(self):
        # Create a .gitignore file in the temporary directory
        gitignore_content = "skip*\nanimal/\n"
        gitignore_path = os.path.join(self.test_dir, ".gitignore")
        
        with open(gitignore_path, "w") as f:
            f.write(gitignore_content)

        # Load .gitignore patterns
        gitignore_spec = load_gitignore(self.test_dir)
        
        # Test that the patterns were loaded correctly
        self.assertTrue(gitignore_spec.match_file("skipme.txt"))
        self.assertTrue(gitignore_spec.match_file("animal/insects/"))
        self.assertFalse(gitignore_spec.match_file("company/apple.html"))

    @patch("codefusion.main.os.walk")
    @patch("codefusion.main.open", new_callable=mock_open)
    def test_combine_code_files_with_gitignore(self, mock_open_file, mock_os_walk):
        # Mock .gitignore patterns
        gitignore_content = "skip*\nanimal/\n"
        gitignore_spec = load_gitignore(self.test_dir)

        # Mock directory structure
        mock_os_walk.return_value = [
            (self.test_dir, ["animal", "company"], ["file1.py", "skipme.txt"]),
            (os.path.join(self.test_dir, "animal"), ["insects"], ["hippo.py"]),
            (os.path.join(self.test_dir, "animal/insects"), [], ["dragonfly.py"]),
            (os.path.join(self.test_dir, "company"), [], ["apple.html"]),
        ]

        # Mock file contents
        file_content = "# Sample content"
        mock_open_file.side_effect = [
            mock_open(read_data=file_content).return_value,
            mock_open(read_data=file_content).return_value,
            mock_open(read_data=file_content).return_value,
        ]

        # Run combine_code_files
        output_file = os.path.join(self.test_dir, "combined_code.txt")
        combine_code_files(root_dir=self.test_dir, output_file=output_file)

        # Assert that open was called with the expected files, skipping ignored ones
        expected_files = [
            os.path.join(self.test_dir, "file1.py"),
            os.path.join(self.test_dir, "company/apple.html")
        ]
        
        # Verify that only the expected files were processed
        actual_files = [call[0][0] for call in mock_open_file.call_args_list]
        for file in expected_files:
            self.assertIn(file, actual_files)
        
        # Verify that ignored files were not processed
        ignored_files = [
            os.path.join(self.test_dir, "skipme.txt"),
            os.path.join(self.test_dir, "animal/hippo.py"),
            os.path.join(self.test_dir, "animal/insects/dragonfly.py")
        ]
        for file in ignored_files:
            self.assertNotIn(file, actual_files)

    def test_combine_code_files_output(self):
        # Create test files in the temporary directory
        test_file_1 = os.path.join(self.test_dir, "file1.py")
        test_file_2 = os.path.join(self.test_dir, "file2.js")
        
        with open(test_file_1, "w") as f:
            f.write("print('Hello from file1')\n")

        with open(test_file_2, "w") as f:
            f.write("console.log('Hello from file2');\n")

        # Run combine_code_files
        output_file = os.path.join(self.test_dir, "combined_code.txt")
        combine_code_files(root_dir=self.test_dir, output_file=output_file, file_types=[".py", ".js"])

        # Verify the output file content
        with open(output_file, "r") as f:
            output_content = f.read()

        # Check that the content includes file headers and content from both files
        self.assertIn("# ==== File:", output_content)
        self.assertIn("print('Hello from file1')", output_content)
        self.assertIn("console.log('Hello from file2')", output_content)

if __name__ == "__main__":
    unittest.main()