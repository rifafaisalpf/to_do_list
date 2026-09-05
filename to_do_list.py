# to do list
import json

def save_tasks():
     with open("tasks.json","w") as file:
          json.dump(tasks,file)

def load_tasks():
     with open("tasks.json","r") as file :
          tasks=json.load(file)
          return tasks

def show_menu():
    print("\n---TO DO LIST---")
    print("1.ADD TASK")
    print("2.VIEW TASK")
    print("3. MARK TASK AS DONE")
    print("4.DELETE TASK")
    print("5.EXIT")

def add_task():
    task=input("ENTER TASK:")
    tasks.append({"task":task,"done":False})
    print("TASK",task,"added ! ")
    save_tasks()


def view_task():
    if not tasks:
        print("NO TASKS YET!")
        return
    print("\nYour Tasks:")
    task_no=1
    complete="❌"
    for task in tasks:
        if task["done"]:
             complete="✅"
        else:
             complete="❌"
        print(task_no,".",task["task"],complete)
        task_no+=1

def mark_task_as_done():
     if not tasks:
          print("NO TASK YET! PLEASE ADD A TASK FIRST")
          
     else:
          view_task()
          try:
               num = int(input("Task number you want to complete: "))
               if (num>0 and num<len(tasks)+1):
                    tasks[num - 1]["done"] = True
                    print(tasks[num-1]["task"],"COMPLETED")
                    save_tasks()
               else:
                    print("TASK NUMBER IS INVALID")
          except ValueError:
               print("PLEASE ENTER A VALID INPUT")
     



def delete_task():
     if not tasks:
          print("NO TASK YET! PLEASE ADD A TASK FIRST")
     else:
          try:
               num = int(input("Task number you want to delete: "))
               if (num>0 and num<len(tasks)+1):
                    print(tasks[num-1]["task"],"DELETED")
                    tasks.remove(tasks[num - 1])
                    save_tasks()
               else:
                    print("TASK NUMBER IS INVALID")
          except ValueError:
               print("PLEASE ENTER A VALID INPUT")
     




try:
     tasks=load_tasks()
except FileNotFoundError:
     tasks=[]
while True:
     show_menu()
     try:
          choice=int(input("ENTER YOUR CHOICE NO:"))
          if (choice<=5 and choice>=1):
               if choice==1:
                    add_task()

               elif choice==2:
                    view_task()

               elif choice==3:
                    mark_task_as_done()

               elif choice==4:
                    delete_task()

               elif choice==5:
                    print("\nGOODBYE! STAY PRODUCTIVE! ✨")
                    break
          else:
               print("INVALID INPUT")
     except ValueError:
          print("PLEASE ENTER A VALID INPUT")

     


         
         
        
         










