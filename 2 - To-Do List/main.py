

def print_menu() -> None:
    print("1 - Add Task")
    print("2 - Remove Task")
    print("3 - Print Task List")
    print("4 - Save Task List")
    print("5 - Load Task List")
    print("4 - Exit")

def task_add(list :list, task :str) -> None:
    list.append(task)

def task_remove(list :list, index :int) -> None:
    list.pop(index)

def task_count(list :list) -> int:
    return len(list)

def task_print_all(list :list) -> None:
    x :int = 0
    counter :int = task_count(list)

    while x < counter:
        print("Item #" + str(x + 1) + " is: " + list[x])
        x = x + 1

def print_new_feature() -> None:
    print("This feature isn't ready yet!")

def main():

    task_list :list = []
    running :bool = True
    user_input :str = ""

    while (running):
        print_menu()
        menu_input = int(input(">"))
        print("\n")

        if menu_input == 1:
            print("What do you want to add to the To-Do list?")
            user_input = input(">")
            task_add(task_list, task=user_input)
            print("\n")

        elif menu_input == 2:
            task_print_all
            print("What do you want to remove from the To-Do list?")
            user_input = input(">")
            task_remove(task_list, index=int(user_input))
            print("\n")

        elif menu_input == 3:
            task_print_all(task_list)
            print("\n")

        elif menu_input == 4:
            print_new_feature()

        elif menu_input == 5:
            print_new_feature()

        elif menu_input == 6:
            print("Exiting the program...")
            pause_check = input(">")
            print("\n")
            running = False
        else:
            print("Please try a different option!")
            print("\n")

  

main()