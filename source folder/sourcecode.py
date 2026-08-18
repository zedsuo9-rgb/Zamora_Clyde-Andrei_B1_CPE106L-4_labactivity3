class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed = False

    def complete_task(self):
        self.is_completed = True

    def __str__(self):
        status = "Done" if self.is_completed else "Pending"
        return f"[{status}] {self.title}: {self.description}"


class ProjectTracker:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: '{task.title}' to {self.project_name}")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete_task()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"Task '{title}' not found.")

    def show_tasks(self):
        print(f"\n--- {self.project_name} Tasks ---")
        for task in self.tasks:
            print(task)
        print("--------------------------\n")


if __name__ == "__main__":
    tracker = ProjectTracker("CPE106L-4 Lab 3 Tasks")

    print("--- TEST CASE 1: Adding Tasks ---")
    task1 = Task("Class Design", "Implement Task and ProjectTracker classes")
    task2 = Task("Code Logic", "Write methods for adding and completing tasks")
    task3 = Task("Run Tests", "Execute three meaningful test cases")

    tracker.add_task(task1)
    tracker.add_task(task2)
    tracker.add_task(task3)

    print("\n--- TEST CASE 2: Displaying All Pending Tasks ---")
    tracker.show_tasks()

    print("--- TEST CASE 3: Completing a Task and Updating Status ---")
    tracker.complete_task("Class Design")
    tracker.show_tasks()