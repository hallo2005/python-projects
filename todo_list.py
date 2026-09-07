print("Welcome to your TO-DO List!")
task = [ ]
choice = ""

while choice != "quit":
    print("1.Add a task\n2.View tasks\n3.Remove a task\n4.Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        new_task = input("Enter a new task: ")
        task.append(new_task)
    elif choice == "2":
        for item in task:
            print(item)
    elif choice == "3":
        for item in task:
            print(item)
        task_to_remove = input("Enter the task you want to remove:")
        task.remove(task_to_remove)
    elif choice == "4":
        print("Exiting the TO-DO List. Goodbye!")
        break
   
print(task)














