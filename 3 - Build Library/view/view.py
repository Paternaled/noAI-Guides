import os

def print_menu_main() -> None:
    print("Main Menu")
    print()
    print("1 - Builds")
    print("2 - Helper Data")
    print("3 - Settings")
    print("4 - Exit")
    print()

def print_menu_helperdata(table_name: str) -> None:

    if table_name == None or table_name == "":
        print("Main Menu --- Helper Data Tables")    
    else:
        print("Main Menu --- Helper Data Tables (" + table_name + ")")
    
    print()
    print("1 - Add Entry")
    print("2 - Edit Entry")
    print("3 - Delete Entry")
    print("4 - Return")
    print()

def print_new_feature() -> None:
    print("This feature isn't ready yet!")

def clear_screen() -> None:
    print("\033[H\033[J", end="")

def pause_program() -> None:
    input()

def request_input_int() -> int:
    result = input(">")
    print()

    try:
        result = int(result)
    except:
        result = None
    
    return result

def request_input_str() -> str:
    result = input(">")
    print()

    try:
        result = str(result)
    except:
        result = None
    
    return result

def print_hello_world() -> None:
    print("Hello World!")
    print()

def print_invalid_input() -> None:
    print("Invalid input!")

def print_return_menu_main() -> None:
    print("Press any key to return to the main menu...")
    pause_program()   

def print_return_menu_main_invalid() -> None:
    print_invalid_input()
    print("Press any key to return to the main menu...")
    pause_program()  

def print_exiting_program() -> None:
    print("Press any key to exit...")
    pause_program()

def print_press_continue():
    print("Press any key to continue...")
    pause_program()

def print_table_startup_results(table_name: str, result_list: list) -> None:
        dash_line = ""
        for symbol in table_name:
            dash_line = dash_line + "--"

        print(table_name)
        print(dash_line)

        i = 0
        for item in result_list:
            print("Table #" + str(i + 1) + ": " + str(result_list[i]))
            i = i + 1

        print()

def choose_table(table_name: str, table_name_list: list) -> str:
    i = 0
    for table in table_name_list:
        print(str(i + 1) + " - " + table_name_list[i])
        i = i + 1

    print()
    print("Which " + table_name + " table do you want to work on?")
    table_selected = request_input_int()

    if table_selected == None:
        return None
    else:
        result = table_name_list[table_selected - 1]
        return result

    




