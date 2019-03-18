scelta=0
n_task=0
task=[]
from sys import argv
fp= argv[1]
txt= open(fp)
for strng in txt.read().splitlines():
    task.append(strng)
    n_task+=1
while scelta!=4:
    print("Task Manager")
    print("1. Insert a new task (a string of text)")
    print("2. Remove a task (by typing a substring of its content)")
    print("3. Show all existing tasks, sorted in alphabetic order")
    print("4. Close the program")
    scelta=int(input("Make your choice: "))
    if(scelta==1):
        task.append(input("Insert task's content: "))
        n_task+=1
    elif(scelta==2):
        if(n_task<=0):
            print("No tasks")
        else:
            ctrl= input("Insert task's substring: ")
            for strng in task:
                if ctrl in strng:
                    task.remove(strng)
    elif(scelta==3):
        if (n_task <= 0):
            print("No tasks")
        else:
            print(sorted(task))
    elif(scelta==4):
        print("The End")
        txt.close()
        txt= open(fp, "w")
        for strng in task:
            txt.write(strng+"\n")
        txt.close()