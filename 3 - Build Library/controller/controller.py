from models import buildmodel 
from models import helperdatamodel


class Controller():

    def run_startup():
        #buildmodel.run_startup()

        helperdatatablecheckresults = helperdatamodel.run_startup()

        i = 0
        for item in helperdatatablecheckresults:
            print("Table #" + str(i + 1) + ": " + str(helperdatatablecheckresults[i]))
            i = i +1
        

    def main():
        pass


