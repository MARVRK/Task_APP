import csv
from abc import ABC, abstractmethod
from Task_Manager import TaskManager, Task
from dataclasses import dataclass

class StoreDataAbstraction(ABC):
    @abstractmethod
    def save_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

@dataclass()
class StoreData(StoreDataAbstraction):
    storage_tasks = TaskManager.storage_tasks


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

td = StoreData()
td.save_file()
