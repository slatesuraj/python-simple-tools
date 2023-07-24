import os
import argparse

class FileManager:
    def create_file(self, file_name):
        with open(file_name, 'w') as file:
            pass

    def delete_file(self, file_name):
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")

    def create_directory(self, dir_name):
        os.makedirs(dir_name, exist_ok=True)

    def delete_directory(self, dir_name):
        try:
            os.rmdir(dir_name)
        except FileNotFoundError:
            print(f"Directory '{dir_name}' not found.")
        except OSError as e:
            print(f"Error: {e}")

    def list_files(self, dir_name="."):
        files = os.listdir(dir_name)
        for file in files:
            print(file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File Management CLI')
    parser.add_argument('command', choices=['create_file', 'delete_file', 'create_directory', 'delete_directory', 'list_files'], help='Choose a command: create_file, delete_file, create_directory, delete_directory, list_files')
    parser.add_argument('--file', help='Specify the file name')
    parser.add_argument('--dir', help='Specify the directory name')

    args = parser.parse_args()

    file_manager = FileManager()

    if args.command == 'create_file':
        if args.file:
            file_manager.create_file(args.file)
        else:
            print("Please specify a file name using the '--file' option.")
    elif args.command == 'delete_file':
        if args.file:
            file_manager.delete_file(args.file)
        else:
            print("Please specify a file name using the '--file' option.")
    elif args.command == 'create_directory':
        if args.dir:
            file_manager.create_directory(args.dir)
        else:
            print("Please specify a directory name using the '--dir' option.")
    elif args.command == 'delete_directory':
        if args.dir:
            file_manager.delete_directory(args.dir)
        else:
            print("Please specify a directory name using the '--dir' option.")
    elif args.command == 'list_files':
        if args.dir:
            file_manager.list_files(args.dir)
        else:
            file_manager.list_files()
