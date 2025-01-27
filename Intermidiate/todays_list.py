task_list = []
print("Welcome to today's working list...")

work = int(input("Enter the number of work today you are doing..."))

for i in range(work):
    tasks = input(f"Enter task {i+1}: ")
    task_list.append(tasks)
    
    print(f"today's tasks are:\n{task_list}")