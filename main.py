from storage import load_tasks
from taskTracker import add_task, view_tasks, update_task, delete_task, mark_task_completed, view_pending_tasks, view_completed_tasks


tasks = load_tasks()

def main():
    choice = 0
    while choice != 8:
        print("***ACADEMIC TASK TRACKER***")
        print("Welcome to the Academic Task Tracker")
        print("Choose an option below:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as completed")
        print("6. View pending tasks")
        print("7. View completed tasks")
        print("8. Exit Program")

        choice = int(input("Enter your choice (Between 1 and 8)>>> "))

        
        if choice == 1:
                add_task(tasks)
            
        elif choice == 2:
                view_tasks(tasks)

        elif choice == 3:
                update_task(tasks)

        elif choice == 4:
                delete_task(tasks)

        elif choice == 5:
                mark_task_completed(tasks)

        elif choice == 6:
                view_pending_tasks(tasks)

        elif choice == 7:
                view_completed_tasks(tasks)

        elif choice == 8:
            print("Exiting the program. Goodbye!")

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
    print("Thank you for using the Academic Task Tracker")

if __name__ == "__main__":
    main()