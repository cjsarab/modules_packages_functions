tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Functions to complete:

## Get a list of uncompleted tasks

def get_uncompleted_tasks(list):
    uncompleted_list = []
    for task in list:
        if task["completed"] == False:
            uncompleted_list.append(task)
    return (uncompleted_list)

## Get a list of completed tasks
def get_completed_tasks(list):
    completed_list = []
    for task in list:
        if task["completed"] == True:
            completed_list.append(task)
    return (completed_list)

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    long_tasks = []
    for task in list:
        if task["time_taken"] >= time:
            long_tasks.append(task)
    return (long_tasks)


## Find a task with a given description
def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task

# Extension (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    for task in list:
        if status == task["completed"]:
            return task

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)