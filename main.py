from storage import load_tasks, save_tasks

tasks = load_tasks()

def add_task():
    # Function to add a new task
    task_id = len(tasks) + 1  # Generate a new task ID
    title = input("What is the title of the task?>>> ")
    course = input("What course is this task for?>>> ")
    description = input("What is the description of the task?>>> ")
    due_date = input("What is the due date of the task? (YYYY-MM-DD)>>> ")
    priority = input("What is the priority of the task? (High, Medium, Low)>>> ")
    status = "Pending"  # Default status for a new task
    task = {
        "id": task_id,
        "title": title,
        "course": course,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": status
    }
    tasks.append(task)
    save_tasks(tasks)  # Save the updated tasks to the JSON file
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return
    else:
        for task in tasks:
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Course: {task['course']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")
            print("-" * 30)

def update_task():
    if len(tasks) == 0:
        print("There are no tasks available!")
        print("Select option 1 to add a new task")
        return
    else:
        for task in tasks:
            print(f"Task id: {task['id']}")
    choose_task = int(input("Select which task you would like to modify (Enter valid task ID)>>>"))

    for task in tasks:
        if choose_task == task['id']:
            print("What do you wish to change?")
            print("1. Title")
            print("2. Course")
            print("3. Description")
            print("4. Due Date")
            print("5. Priority")
            print("6. Status")
            choose_part_to_change = int(input("Enter your option here>>>"))
            if choose_part_to_change == 1:
                new_title = input("Enter the new title>>>")
                task['title'] = new_title
                print("Title updated successfully!")

            elif choose_part_to_change == 2:
                new_course = input("Enter the new course>>>")
                task['course'] = new_course
                print("Course updated successfully!")

            elif choose_part_to_change == 3:
                new_description = input("Enter the new description>>>")
                task['description'] = new_description
                print("Description updated successfully!")

            elif choose_part_to_change == 4:
                new_due_date = input("Enter the new due date (YYYY-MM-DD)>>>")
                task['due_date'] = new_due_date
                print("Due date updated successfully!")

            elif choose_part_to_change == 5:
                new_priority = input("Enter the new priority (High, Medium, Low)>>>")
                task['priority'] = new_priority
                print("Priority updated successfully!")

            elif choose_part_to_change == 6:
                new_status = input("Enter the new status (Pending, Completed)>>>")
                task['status'] = new_status
                print("Status updated successfully!")

            else:
               print("Invalid option. Please enter a number between 1 and 6.")
               return       

            save_tasks(tasks)  # Save the updated tasks to the JSON file
            return

            
    else:
        print("Invalid task ID. Please enter a valid task ID.")
        return
        
       # 
def delete_task():
    if len(tasks) == 0:
        print("There are no tasks available!")
        print("Select option 1 to add a new task")
        return
    else:
        for task in tasks:
            print(f"Task id: {task['id']}")
    choose_task = int(input("Select which task you would like to delete (Enter valid task ID)>>>"))

    for task in tasks:
        if choose_task == task['id']:
            tasks.remove(task)
            print("Task deleted successfully!")
            save_tasks(tasks)  # Save the updated tasks to the JSON file
            return
    else:
        print("Invalid task ID. Please enter a valid task ID.")


def mark_task_completed():
    if len(tasks) == 0:
        print("There are no tasks available!")
        print("Select option 1 to add a new task")
        return
    else:
        for task in tasks:
            print(f"Task id: {task['id']}")
    choose_task = int(input("Select which task you would like to mark as completed (Enter valid task ID)>>>"))

    for task in tasks:
        if choose_task == task['id']:
            task['status'] = "Completed"
            save_tasks(tasks)  # Save the updated tasks to the JSON file
            print("Task marked as completed successfully!")
            return
    else:
        print("Invalid task ID. Please enter a valid task ID.")


def view_pending_tasks():
    pending_tasks = [task for task in tasks if task['status'] == "Pending"]
    if len(pending_tasks) == 0:
        print("No pending tasks available.")
        return
    else:
        for task in pending_tasks:
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Course: {task['course']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")
            print("-" * 30)


def view_completed_tasks():
    completed_tasks = [task for task in tasks if task['status'] == "Completed"]
    if len(completed_tasks) == 0:
        print("No completed tasks available.")
        return
    else:
        for task in completed_tasks:
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Course: {task['course']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")
            print("-" * 30)
            




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
                add_task()
            
        elif choice == 2:
                view_tasks()

        elif choice == 3:
                update_task()

        elif choice == 4:
                delete_task()

        elif choice == 5:
                mark_task_completed()

        elif choice == 6:
                view_pending_tasks()

        elif choice == 7:
                view_completed_tasks()

        elif choice == 8:
            print("Exiting the program. Goodbye!")

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
    print("Thank you for using the Academic Task Tracker")

if __name__ == "__main__":
    main()