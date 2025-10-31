print("""\n===TO DO LIST MENU===
1. View To-Do List
2. Add Task
3. Edit Task
4. Remove task
5. Exit""")


task = ['Doing Lab Activity', 'Grocery', 'Coffee with Friends', 'Study Automata', 'Practice coding']


while True:
  choice = input("\nChoose an option to perform (1-5): ")


  match choice:
      case '1':
          if len(task) == 0:
              print("Your To-Do list is empty.")
          else:
              print("\nYour To-Do List:")
              for i, t in enumerate(task, start=1):
                  print(f"{i}. {t}")


      case '2':
          new_task = input("Enter a new task: ")
          task.append(new_task)
          print(f'Task "{new_task}" is added.')


      case '3':
          if len(task) == 0:
              print("Your to-do list is empty.")
          else:
              for i, t in enumerate(task, start=1):
                  print(f"{i}. {t}")
              try:
                  task_num = int(input("\nEnter the task number to edit: "))
                  if 1 <= task_num <= len(task):
                      new_task = input("Enter the new task: ")
                      old_task = task[task_num - 1]
                      task[task_num - 1] = new_task
                      print(f"Task '{old_task}' updated to '{new_task}'.")
                  else:
                      print("Invalid task number.")
              except ValueError:
                  print("Please enter a valid number.")

      case '4':
          if len(task) == 0:
              print("Your to-do list is empty.")
          else:
              for i, t in enumerate(task, start=1):
                  print(f"{i}. {t}")
              try:
                  task_num = int(input("\n Enter the task number to remove: "))
                  if 1 <= task_num <= len(task):
                      removed = task.pop(task_num - 1)
                      print(f"Task '{removed}' removed.")
                  else:
                      print("Invalid task number.")
              except ValueError:
                  print("Please enter a valid number.")

      case '5':
          print("Exit the program.")
          break;

