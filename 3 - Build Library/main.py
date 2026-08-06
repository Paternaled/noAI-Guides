from controller.controller import Controller


def main():

#Reachout to the controller to check for all of the tables and configuration files
    controller = Controller
    controller.run_startup()

    running :bool = True

    while (running):

        controller.loop_main()

        running = False

main()