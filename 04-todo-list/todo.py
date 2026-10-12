
DONE_MARK = " (done)"
tasks = []
while True:
    print("1) Add task")
    print("2) Show tasks")
    print("3) Remove task")
    print("4) Mark task as done")
    print("5) Exit") 
    user = int(input(" enter your option: "))
    if user == 1:
        task = input("enter your task: ")
        tasks.append(task)
    elif user == 2:
        if len(tasks)>= 1:
            for number, task in enumerate(tasks , start= 1):
                print(f"{number} : {task}")
        else:
            print(" no task ")
    elif user == 3:
        delt = int(input("what task? "))
        if 1 <= delt <= len(tasks):
            tasks.pop(delt-1)
        else:
            print(" not exist ")


    elif user == 4:
        done = int(input(" Select the task you have finished. "))
        if 1 <= done <= len(tasks):
            if tasks[done-1].endswith(DONE_MARK):
                print("It has already been checked.")
            else:
                tasks[done-1] += DONE_MARK
        else:
            print(" no task")
    elif user == 5:
            break
    else:
        print(" error")
        

