# Python Simple Cli Tools

Hello.


# Installation
```
pip install fire
```

# Tools

## File Manager

A file management CLI can help users perform various file-related operations, such as creating, deleting, moving, and listing files and directories. Let's create a simple file management CLI using Python and the argparse library, which is included in Python's standard library.

You can use the following commands with the CLI:
   To create a new file:  
   ```
   python file_manager.py create_file --file <file_name>
   ```
   To delete a file: 
   ```
   python file_manager.py delete_file --file <file_name>
   ```
   To create a new directory: 
   ```
   python file_manager.py create_directory --dir <directory_name>
   ```
   To delete a directory: 
   ```
   python file_manager.py delete_directory --dir <directory_name>
   ```
   To list files in the current directory or a specified directory: 
   ```
   python file_manager.py list_files --dir <directory_name>
   ```

## Task Manager
This CLI will allow users to add tasks, view the task list, mark tasks as completed, and delete tasks.

You can use the following commands with the CLI:
 To add a new task: 
   ```
   python task_manager.py add --task "Write a report"
   ```
   To view the list of tasks: 
   ```
   python task_manager.py view
   ```
   To mark a task as completed (replace <task_index> with the index of the task from the list): 
   ```
   python task_manager.py complete --index <task_index>
   ```
   To delete a task (replace <task_index> with the index of the task from the list): 
   ```
   python task_manager.py delete --index <task_index>
   ```
This task management CLI allows users to manage their tasks easily from the command line. It provides a simple yet effective interface for organizing and tracking tasks without the need for a full-fledged task management application.
