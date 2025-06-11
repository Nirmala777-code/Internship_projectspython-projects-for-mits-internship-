todo_list = []

def show_menu():
    print("\n📋 To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task = input("Enter your task: ")
        todo_list.append({"task": task, "done": False})
        print("✅ Task added!")

    elif choice == "2":
        print("\n📝 Your Tasks:")
        for i, t in enumerate(todo_list):
            status = "✅ Done" if t["done"] else "⏳ Pending"
            print(f"{i + 1}. {t['task']} - {status}")

    elif choice == "3":
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]["done"] = True
            print("✔️ Marked as done!")
        else:
            print("❌ Invalid task number.")

    elif choice == "4":
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"🗑️ Deleted: {removed['task']}")
        else:
            print("❌ Invalid task number.")

    elif choice == "5":
        print("👋 Exiting To-Do List. Have a productive day!")
        break

    else:
        print("❌ Invalid option. Please choose 1-5.")