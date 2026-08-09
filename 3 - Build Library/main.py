from controller.maincontroller import MainController


def main():

#Reachout to the controller to check for all of the tables and configuration files
    main_controller = MainController
    main_controller.run_startup()

    running :bool = True

    while (running):

        main_controller.loop_main()

        running = False

main()