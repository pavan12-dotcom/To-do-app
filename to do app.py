# Simple To-Do App in Python

tasks = []

def show_menu():
    print("\n--- To-Do App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ '{task}' added to your list.")

    elif choice == "2":
        if not tasks:
            print("📂 No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("❌ No tasks to remove.")
        else:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑️ Removed '{removed}'")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("⚠️ Invalid choice, try again.")