import json

def load():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def saved(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def displayfunc():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Delete Task")
    print("4. View Tasks")
    print("5. Exit")
    print(" ")

def addtolist(tasks):
    task = input("Enter task description: ")
    tasks.append({"description": task, "completed": False})
    saved(tasks)
    print(" ")

def completedtasks(tasks):
    task_index = int(input("Enter task index to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        saved(tasks)
    else:
        print("Invalid task index.")

def delete(tasks):
    task_index = int(input("Enter task index to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        saved(tasks)
    else:
        print("Invalid task index.")

def display(tasks):
    print("Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{i}. {task['description']} ({status})")
    print(" ")
def main():
    tasks = load()

    while True:
        displayfunc()
        skibidi = input("Enter your task: ")

        if skibidi == '1':
            addtolist(tasks)
        elif skibidi == '2':
            completedtasks(tasks)
        elif skibidi == '3':
            delete(tasks)
        elif skibidi == '4':
            display(tasks)
        elif skibidi == '5':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()