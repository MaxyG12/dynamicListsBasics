print("ToDo List Manager")
print()

toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("Do you want to view, add, or edit your to do list?: ")
  if menu == "view":
    printList()
  elif menu == "add":
    item = input("What do you want to add?: ")
    toDoList.append(item)
  elif menu == "edit":
    item = input("What do you want to remove?: ")
    if item in toDoList:
      toDoList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()
  