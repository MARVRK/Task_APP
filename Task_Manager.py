from dataclasses import dataclass
from typing import List
import csv


@dataclass
class Task:
    name: str
    priority: int
    duration: int
    status: str = "in progress"


class TaskManager:
    storage_tasks : List[Task] = []
    total_tasks = 0
    task_completed = 0
    average_not_completed_tasks = 0

    def add_task(self, task: Task):
        self.total_tasks += 1
        self.storage_tasks.append(task)

    def change_status(self, task_name: str, new_status: str):
        name_storage = []
        for x in self.storage_tasks:
            name_storage.append(x.name)

        if task_name in name_storage:
            for x in self.storage_tasks:
                if x.name == task_name:
                    x.status = new_status
        else:
            raise ValueError("Not task found")

        if new_status.lower() == "done":
            self.task_completed += 1

    def top_task_to_do(self):
        for data_status in self.storage_tasks:
            if data_status.status == "in progress":
                top_tasks_to_do = []
                priorities = []

                for data_object in self.storage_tasks:
                    priorities.append(data_object.priority)

                for data_task in self.storage_tasks:
                    if data_task.priority == min(priorities):
                        top_tasks_to_do.append(data_task)

                num_task = enumerate(top_tasks_to_do)
                return min(num_task)


    def statistics(self):
        time_storage = 0
        tasks_left = self.total_tasks - self.task_completed

        for cursor in self.storage_tasks:
            if cursor.status != "Done":
                time_storage += cursor.duration

        if tasks_left != 0:
            average_time = time_storage // tasks_left
            average_time_hours = average_time // 60
            average_time_minutes = average_time % 60

            return (f"Completed_task: {self.task_completed} \nTotal_tasks: {self.total_tasks} \nTasks_Left: {tasks_left}"
                    f"\nAverage_Time_Incompleted_tasks: {average_time_hours} h. {average_time_minutes} min.")

        return (f"Completed_task: {self.task_completed} \nTotal_tasks: {self.total_tasks} \nTasks_Left: {tasks_left}"
                f"\nAverage_Time_Incompleted_tasks: {None}")


    def save_file(self):
        rows = []
        header = ["Task_Name", "Priority", "Duration in Min.", "Status"]
        for data in self.storage_tasks:
            rows.append([data.name, data.priority, data.duration, data.status])

        with open("data.csv", "w", encoding="UTF8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)


    def read_file(self):
        with open("data.csv", "r", encoding="UTF8") as f:
            reader = csv.reader(f)
            for x in reader:
                print(x)



cp = Task(name="Shopping", priority=2, duration=125)
cp1 = Task(name="Wash Car", priority=1, duration=40)
cp3 = Task(name="Doing Somthing", priority=3, duration=75)
task = TaskManager()
task.add_task(cp)
task.add_task(cp1)
task.add_task(cp3)
task.change_status("Doing Somthing", "Done")
print(task.top_task_to_do())
print(task.statistics())
#task.save_file()
task.read_file()