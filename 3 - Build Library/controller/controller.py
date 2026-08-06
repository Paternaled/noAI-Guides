import models.buildmodel as buildmodel
import models.helperdatamodel as helperdatamodel


class Controller():

    def run_startup():
        helperdatatablecheckresults = helperdatamodel.run_startup()
        buildtableresults = buildmodel.run_startup()
        
        print("Helper Data Tables")
        print("-------------------")

        i = 0
        for item in helperdatatablecheckresults:
            print("Table #" + str(i + 1) + ": " + str(helperdatatablecheckresults[i]))
            i = i + 1

        print()
        print("Build Tables")
        print("---------------")

        i = 0
        for item in buildtableresults:
            print("Table #" + str(i + 1) + ": " + str(buildtableresults[i]))
            i = i + 1
        