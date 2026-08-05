import models.buildmodel as buildmodel
import models.helperdatamodel as helperdatamodel


class Controller():

    def run_startup():
        helperdatatablecheckresults = helperdatamodel.run_startup()

        i = 0
        for item in helperdatatablecheckresults:
            print("Table #" + str(i + 1) + ": " + str(helperdatatablecheckresults[i]))
            i = i +1


        #buildmodel.run_startup()


