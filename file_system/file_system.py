# file_system/file_system.py

import os
import json

class InMemoryFileSystem:
    def __init__(self):
        # Initialize the file system with a root directory and an empty structure
        self.current_directory = '/'
        self.file_system_structure = {}

    """
        Create a new directory.

        If the specified directory does not already exist, it is created.
        If the directory already exists, an error message is displayed.

        Parameters:
        - directory (str): The name of the directory to create.
    """
    def mkdir(self, directory):
        if directory not in self.file_system_structure:
            self.file_system_structure[directory] = {}
        else:
            print(f"Error: Directory '{directory}' already exists.")

        """
        Change the current directory.

        Allows navigation to the parent directory ('..'), absolute paths ('/'),
        and relative paths within the current directory.

        Parameters:
        - path (str): The path to navigate to.
        """
    def cd(self, path):
        if path == '..':
            # Move to the parent directory
            self.current_directory = os.path.dirname(self.current_directory)
        elif path.startswith('/'):
            # Move to an absolute path
            self.current_directory = path
        else:
            # Move to a relative path
            new_path = os.path.join(self.current_directory, path)
            self.current_directory = os.path.normpath(new_path)

        """
        List the contents of a directory.

        If no directory is specified, it lists the contents of the current directory.
        Displays an error message if the specified directory does not exist.

        Parameters:
        - directory (str, optional): The directory to list the contents of.
        """
    def ls(self, directory=None):
        if directory is None:
            directory = self.current_directory[1:]

        if directory == '':
            contents = list(self.file_system_structure.keys())
            print(f"Contents of '/': {contents}")
        else:
            if directory in self.file_system_structure:
                contents = list(self.file_system_structure[directory].keys())
                print(f"Contents of {directory}: {contents}")
            else:
                print(f"Error: Directory '{directory}' does not exist.")

        """
        Create a new empty file.

        If the specified file does not already exist, it is created.
        If the file already exists, an error message is displayed.

        Parameters:
        - file_name (str): The name of the file to create.
        """
    def touch(self, file_name):
        current_path = os.path.join(self.current_directory, file_name)
        if current_path not in self.file_system_structure:
            self.file_system_structure[current_path] = ""
        else:
            print(f"Error: File '{file_name}' already exists.")

        """
        Write text to a file.

        If the specified file exists, its content is replaced with the new text.
        If the file does not exist, an error message is displayed.

        Parameters:
        - content (str): The text to write to the file.
        - file_name (str): The name of the file to write to.
        """
    def echo(self, content, file_name):
        current_path = os.path.join(self.current_directory, file_name)
        if current_path in self.file_system_structure:
            self.file_system_structure[current_path] = content
        else:
            print(f"Error: File '{file_name}' does not exist.")

        """
        Display the contents of a file.

        If the specified file exists and is not a directory, its contents are displayed.
        If the file does not exist or is a directory, an error message is displayed.

        Parameters:
        - file_path (str): The path to the file.
        """
    def cat(self, file_path):
        full_path = os.path.join(self.current_directory, file_path)

        if full_path not in self.file_system_structure:
            print(f"Error: File '{full_path}' does not exist.")
            return

        if not self.file_system_structure[full_path]:
            print(f"Error: '{full_path}' is not a file.")
            return

        contents = self.file_system_structure[full_path]
        print(f"Contents of {full_path}: {contents}")

        """
        Move a file or directory to another location.

        If the source path exists, its content is moved to the destination path.
        If the source path does not exist, an error message is displayed.

        Parameters:
        - source_path (str): The path of the file or directory to move.
        - destination_path (str): The destination path.
        """
    def mv(self, source_path, destination_path):
        if source_path in self.file_system_structure:
            content = self.file_system_structure.pop(source_path)
            self.file_system_structure[destination_path] = content
        else:
            print(f"Error: Source path '{source_path}' does not exist.")

        """
        Copy a file or directory to another location.

        If the source path exists, its content is copied to the destination path.
        If the source path does not exist, an error message is displayed.

        Parameters:
        - source_path (str): The path of the file or directory to copy.
        - destination_path (str): The destination path.
        """
    def cp(self, source_path, destination_path):
        if source_path in self.file_system_structure:
            content = self.file_system_structure[source_path]
            self.file_system_structure[destination_path] = content
        else:
            print(f"Error: Source path '{source_path}' does not exist.")

        """
        Remove a file or directory.

        If the specified path exists, it is removed from the file system.
        If the path does not exist, an error message is displayed.

        Parameters:
        - path (str): The path of the file or directory to remove.
        """
    def rm(self, path):
        if path in self.file_system_structure:
            del self.file_system_structure[path]
        else:
            print(f"Error: Path '{path}' does not exist.")

        """
        Save the current state of the file system to a file.

        The state includes the current directory and the file system structure.

        Parameters:
        - file_path (str): The path to the file where the state will be saved.
        """
    def save_state(self, file_path):
        state_data = {
            "current_directory": self.current_directory,
            "file_system_structure": self.file_system_structure
        }

        with open(file_path, 'w') as file:
            json.dump(state_data, file)

        """
        Load a previously saved state from a file.

        The state includes the current directory and the file system structure.

        Parameters:
        - file_path (str): The path to the file from which the state will be loaded.
        """
    def load_state(self, file_path):
        with open(file_path, 'r') as file:
            state_data = json.load(file)

        self.current_directory = state_data["current_directory"]
        self.file_system_structure = state_data["file_system_structure"]
