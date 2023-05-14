from AGV_ToolKit.PathPlanning import PathPlanning
from AGV_ToolKit.MoveCalculation import MoveCalculation
from AGV_ToolKit.MoveSimulation import MoveSimulation

class AGV(PathPlanning, MoveCalculation, MoveSimulation):
    pass

robot = AGV()
robot.setState("A")
robot.pathPlanningStep("D", status=True)