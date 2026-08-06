
import models.buildmodel as buildmodel
import models.helperdatamodel as helperdatamodel
import view.view as view

class Controller():

    def __init__(self):
        pass

#Tell the models to create their tables if they don't exist
#The controller checks to make sure everything ran correctly and passes the information to the view

    def run_startup():

        view.clear_screen()

        helperdatatablecheckresults = helperdatamodel.run_startup()
        buildtableresults = buildmodel.run_startup()

        view.print_table_startup_results("Helper Data Table", helperdatatablecheckresults)
        view.print_table_startup_results("Build Tables", buildtableresults)

        view.print_press_continue()
        view.clear_screen()

    def loop_main() -> None:

        running: bool = True

        while(running):

            view.clear_screen()

            view.print_menu_main()
            menu_input: int = view.request_input_int()

            if menu_input == 1:
                view.print_new_feature()
                view.print_press_continue()

            elif menu_input == 2:
                Controller.loop_helperdata()

            elif menu_input == 3:
                view.print_new_feature()
                view.print_press_continue()

            elif menu_input == 4:
                view.print_exiting_program()
                view.clear_screen()
                running = False

            else:
                view.print_invalid_input()
                view.print_press_continue()


    def loop_helperdata() -> None:

        view.clear_screen()

        table_name_list = helperdatamodel.table_list()
        table_selected = view.choose_table("Helper Data", table_name_list)

        running: bool = True

        if table_selected == None:
            view.print_return_menu_main_invalid()
            running = False

        while(running):

            view.clear_screen()

            view.print_menu_helperdata(table_selected)
            menu_input: int = view.request_input_int()

            if menu_input == 1:
                view.print_new_feature()
                view.print_press_continue()

            elif menu_input == 2:
                view.print_new_feature()
                view.print_press_continue()

            elif menu_input == 3:
                view.print_new_feature()
                view.print_press_continue()
                

            elif menu_input == 4:
                view.print_return_menu_main()
                running = False

            else:
                view.print_invalid_input()
                view.print_press_continue()