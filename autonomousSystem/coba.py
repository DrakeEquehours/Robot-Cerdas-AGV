from PathPlanning import PathPlanning
from MoveCalculation import MoveCalculation
from MoveSimulation import Simulation

class AGV(PathPlanning, MoveCalculation, Simulation):
    pass



robot = AGV()
robot.setState("A")
robot.pathPlanningStep("D", status=True)
