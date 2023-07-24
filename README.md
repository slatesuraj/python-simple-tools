# Python Simple Cli Tools

Hello.


# Installation
```
pip install fire
pip install forex-python # for currency converter tool
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

## Currency Converter
This CLI will allow users to convert between different currencies using real-time exchange rates.

You can use the following command with the CLI:
To convert an amount from one currency to another (replace `<amount>`, `<from_currency>`, and `<to_currency>` with the desired values):
```
python currency_converter.py <amount> <from_currency> <to_currency>
```
For example, to convert 100 USD to EUR, use:
```
python currency_converter.py 100 USD EUR
```
The CLI will provide the converted amount based on real-time exchange rates fetched from the forex-python library.

Please note that real-time exchange rates can fluctuate, so the converted amount may vary slightly depending on the time of conversion. The forex-python library updates its rates regularly to provide the latest information.
