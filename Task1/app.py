def task():
    task = []
    print("Welcome to the To-Do List App!")
     
    total_tasks = int(input("Enter the number of tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i}: ")
        task.append(task_name)
        
    print(f"today's tasks are:\n{task}")
    
    while True:
        opration = int(input("Enter 1-add\n 2-delete\n3-update\n4-complete\n5-View\n6-exit/stop\n"))
        if opration == 1:
            add = input("Enter the task you want to add: ")
            task.append(add)
            print(f"task added successfully\n{task}")
        elif opration == 2:
            delete = input("Enter the task you want to delete: ")
            if delete in task:
                task.remove(delete)
                print(f"task deleted successfully\n{task}")
            else:
                print("task not found!")
        elif opration == 3:
            update = input("Enter the task you want to update: ")
            if update in task:
                new_task = input("Enter the new task: ")
                index = task.index(update)
                task[index] = new_task
                print(f"task updated successfully\n{task}")
            else:
                print("task not found!")
        elif opration == 4:
            complete = input("Enter the task you want to mark as complete: ")
            if complete in task:
                index = task.index(complete)
                task[index] = "✔ " + complete
                print(f"task marked as complete\n{task}")
            else:
                print("task not found!")
        elif opration == 5:
            print(f"Today's tasks are:\n{task}")
            
        elif opration == 6:
            print("Exiting the To-Do List App. Goodbye!")
            break       
    return

task()
