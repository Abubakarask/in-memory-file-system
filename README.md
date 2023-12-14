# In-Memory File System

## Overview

This project implements an in-memory file system with various functionalities. The file system supports operations such as creating directories, changing the current directory, listing contents, creating files, writing to files, moving files or directories, copying files or directories, and removing files or directories. Additionally, there is functionality for saving and loading the state of the file system.

## File System Structure

The in-memory file system maintains a structure that represents directories and files. Each directory can contain subdirectories and files. The root directory is denoted by `/`.

## Implemented Commands

### 1. `mkdir <directory>`

- Create a new directory.
- Example:
```bash
mkdir documents
```

### 2. `cd <path>`

- Create a new directory.
- Example:
```bash
cd documents
```

### 3. `ls [directory]`

List the contents of the current directory or a specified directory.
Example:
- Example:
```bash
ls
ls documents
```

### 4. `touch <file_name>`

- Create a new empty file.
- Example:
```bash
touch notes.txt
touch server.js
```

### 5. `echo <content> > <file_name>`

- Write text to a file.
- Example:
```bash
echo 'Hello, World!' > notes.txt
```

### 6. `mv <source_path> <destination_path>`

- Move a file or directory to another location.
- Example:
```bash
mv documents/notes.txt backup/
```

### 7. `cp <source_path> <destination_path>`

- Copy a file or directory to another location.
- Example:
```bash
cp documents/report.txt backup/
```

### 8. `rm <path>`

- Removes a file or directory.
- Example:
```bash
rm \documents\notes.txt 
```

### 9. `save_state <file_path>`

- Save the current state of the file system to a file.
- Example:
```bash
save_state state.json
```

### 10. `load_state <file_path>`

- Load a previously saved state from a file.
- Example:
```bash
load_state state.json
```

### 11. `cat <file_path>`

- Display the contents of a file.
- Example:
```bash
cat server.js
```

### 11. `exit`

- To exit from the command terminal.
- Example:
```bash
exit
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/Abubakarask/in-memory-file-system.git
cd in-memory-file-system
```

2. Run the file system:
```bash
python main.py
```

3. Enter commands in the terminal and observe the file system's behavior.
