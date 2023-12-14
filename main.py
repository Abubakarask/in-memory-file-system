# main.py

from file_system.file_system import InMemoryFileSystem

"""
    Display available commands and their descriptions.
"""
def print_help():
    print("Available commands:")
    print("  mkdir <directory>: Create a new directory.")
    print("  cd <path>: Change the current directory.")
    print("  ls [directory]: List contents of the current or specified directory.")
    print("  touch <file_name>: Create a new empty file.")
    print("  echo <content> > <file_name>: Write text to a file.")
    print("  mv <source_path> <destination_path>: Move a file or directory to another location.")
    print("  cp <source_path> <destination_path>: Copy a file or directory to another location.")
    print("  rm <path>: Remove a file or directory.")
    print("  save_state <file_path>: Save the current state of the file system to a file.")
    print("  load_state <file_path>: Load a previously saved state from a file.")
    print("  exit: Exit the program.")

def main():
    # Create an instance of the InMemoryFileSystem class
    file_system = InMemoryFileSystem()

    while True:
        # Get user input and split it into a list of words
        command = input(f"{file_system.current_directory} $ ").split()

        # Check if the user entered any command
        if not command:
            continue

        # Extract the first word (command) and convert it to lowercase
        action = command[0].lower()

        # Check which command the user entered
        if action == 'exit':
            # Exit the program
            break
        elif action == 'help':
            # Display available commands
            print_help()
        elif action == 'ls':
            # List contents of the current or specified directory
            file_system.ls(command[1] if len(command) > 1 else None)
        elif action == 'save_state':
            # Save the current state of the file system to a file
            file_system.save_state(command[1])
        elif action == 'load_state':
            # Load a previously saved state from a file
            file_system.load_state(command[1])
        elif action == 'echo':
            # Join the input and split on whitespace, preserving quoted content
            command_str = ' '.join(command[1:])
            command_parts = []
            inside_quotes = False
            current_part = ""

            # Iterate over characters in the command string
            for char in command_str:
                if char == ' ' and not inside_quotes:
                    if current_part:
                        command_parts.append(current_part)
                        current_part = ""
                elif char == "'":
                    inside_quotes = not inside_quotes
                else:
                    current_part += char

            if current_part:
                command_parts.append(current_part)

            # Check if the command has the expected format
            if len(command_parts) < 3 or command_parts[1] != '>':
                print("Error: Invalid 'echo' command format.")
            else:
                # Extract content and file name
                content = ' '.join(command_parts[:2])
                file_name = command_parts[-1]
                # Call the echo method in the file system
                file_system.echo(content, file_name)
        else:
            # For other commands, join the arguments and call the corresponding method
            arguments = ' '.join(command[1:])
            try:
                # Dynamically call the corresponding method in the file system
                eval(f"file_system.{action}('{arguments}')")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    # Run the main function if this script is executed directly
    main()
