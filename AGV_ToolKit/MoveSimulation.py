from time import sleep, time
class MoveSimulation:
    def __init__(self) -> None:
        pass
    @staticmethod
    def runPlan(plan):
        list = []
        for i in range(len(plan)):
            # print("jarak:", plan[i][1])
            if not plan[i-1][2] == plan[i][2] and i>0:
                # print(plan[i][2])
                list.append([0,plan[i][2]])
            list.append([1,plan[i][1]])
        return list

    @staticmethod
    def simulation(timer):
        for i in timer:
            for j in range(i[1]):
                print('status:', i[0], "Rotation: " if i[0] == 0 else "Distance: " , j)
                sleep(0.05)
    
