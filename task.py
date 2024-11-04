class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Описание: {self.description}, Срок: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Неверный индекс задачи.")

    def list_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        if not pending_tasks:
            print("Нет текущих (не выполненных) задач.")
        else:
            for i, task in enumerate(pending_tasks, 1):
                print(f"{i}. {task}")


# Пример использования TaskManager
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2023-10-12")
task_manager.add_task("Подготовить отчет", "2023-10-15")

print("Текущие задачи:")
task_manager.list_pending_tasks()

task_manager.mark_task_completed(0)

print("\nПосле выполнения первой задачи:")
task_manager.list_pending_tasks()