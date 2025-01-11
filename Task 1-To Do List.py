tasks = []

while True:
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Mark Task as Not Done")
    print("5. Remove Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print()
        try:
            n_tasks = int(input("How many tasks do you want to add? "))
            for i in range(n_tasks):
                task = input(f"Enter task {i + 1}: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '2':
        print("\nTasks:")
        if tasks:
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")
        else:
            print("No tasks found.")

    elif choice == '3':
        try:
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '4':
        try:
            task_index = int(input("Enter the task number to mark as not done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = False
                print("Task marked as not done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '5':
        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task['task']}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '6':
        print("Exiting the To-Do List.")
        break

    else:
        print("Invalid choice. Please try again.")
