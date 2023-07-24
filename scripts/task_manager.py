import argparse

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Task List:")
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{i}. {task['task']} - {status}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['completed'] = True
            print(f"Task '{self.tasks[task_index - 1]['task']}' marked as completed.")
        else:
            print("Invalid task index. Please provide a valid task number.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task_name = self.tasks[task_index - 1]['task']
            del self.tasks[task_index - 1]
            print(f"Task '{task_name}' deleted successfully.")
        else:
            print("Invalid task index. Please provide a valid task number.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Task Management CLI')
    parser.add_argument('command', choices=['add', 'view', 'complete', 'delete'], help='Choose a command: add, view, complete, delete')
    parser.add_argument('--task', help='Specify the task description')
    parser.add_argument('--index', type=int, help='Specify the task index for complete or delete commands')

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == 'add':
        if args.task:
            task_manager.add_task(args.task)
        else:
            print("Please specify a task description using the '--task' option.")
    elif args.command == 'view':
        task_manager.view_tasks()
    elif args.command == 'complete':
        if args.index:
            task_manager.mark_completed(args.index)
        else:
            print("Please specify a task index using the '--index' option.")
    elif args.command == 'delete':
        if args.index:
            task_manager.delete_task(args.index)
        else:
            print("Please specify a task index using the '--index' option.")
