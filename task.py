import datetime

def main():
    tasks = []  # Initialize an empty list to store tasks
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please choose a valid option.")

def add_task(tasks):
    task_name = input("Enter task name: ")
    timestamp = datetime.datetime.now()
    tasks.append({"name": task_name, "completed": False, "timestamp": timestamp})
    print("Task added successfully!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print_task_list(tasks)

def mark_completed(tasks):
    list_tasks(tasks)
    task_number = input("Enter the task number to mark as completed: ")
    try:
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            tasks[task_number - 1]["completion_time"] = datetime.datetime.now()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            timestamp = task["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            completion_time = task.get("completion_time", "")
            completion_info = f",Task completed on {completion_time.strftime('%Y-%m-%d %H:%M:%S')}" if completion_time else ""
            file.write(f"{task['name']},{task['completed']},{timestamp}{completion_info}\n")

def print_task_list(tasks):
    print("\nTask List:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not Completed"
        timestamp = task["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        completion_info = f"Task completed on {task['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}" if task["completed"] else ""
        print(f"{index}. {task['name']} - {status} (Added on {timestamp}) {completion_info}")

if name == "main":
    main()