
from collections import deque

class Task(object):
    def __init__(self, taskDesc, hasPriority):
        self.taskDesc = taskDesc
        self.hasPriority = hasPriority
    def __str__(self):
        return "Task: {0}, Priority: {1}".format(self.taskDesc, self.hasPriority)

def add_task(tasklist, tasks, haspriority):
    return

def complete_task(task, tasklist):
    return

def print_tasks(tasklist):
    return print(tasklist)

def main():
    #add code here
    tasklist = deque()
    new_task = ["DJ", "Flowers", "Catering", "Church"]
    priorities = ["Y", "N", "Y", "N"]
    print(Task("DJ", True))

if __name__ == "__main__":
    main()