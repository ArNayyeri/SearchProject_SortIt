from Problem import Problem
from State import State
import os

GUI_ENABLE = True


class Solution:
    def __init__(self, state: State, problem: Problem):
        self.state = state
        self.problem = problem

    def print_path(self):  # this for show path of every search how it's done
        queue = []
        state = self.state.parent
        while state is not None:
            queue.insert(0, state)
            state = state.parent
        print('Init State')
        self.problem.print_state(queue[0])
        with open('.\\gui\\AI-GUI_Data\\StreamingAssets\\Test Input.txt', 'w') as file:
            file.write(self.problem.get_state_for_gui(queue[0]))
            file.close()
        actions = ""
        for index, state in enumerate(queue[1:]):
            print('---------\n')
            print('previous action : ' + str(state.prev_action) + "\n")
            actions += 'P' + str(state.prev_action[0] + 1) + ',' + 'p' + str(state.prev_action[1] + 1) + '\n'
            print(f'next step => {index + 1}')
            self.problem.print_state(state)
        with open('.\\gui\\AI-GUI_Data\\StreamingAssets\\Test Input.txt', 'a') as file:
            file.write(actions)
            file.close()
        print('---------\n')
        print('Solution State')
        self.problem.print_state(self.state)

    def execute_gui(self):
        absolute_path = os.path.dirname(__file__)
        relative_path = "gui\AI-GUI.exe"
        full_path = os.path.join(absolute_path, relative_path)
        if GUI_ENABLE:
            os.startfile(full_path)
