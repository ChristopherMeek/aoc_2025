import pulp
from .parser import MachineState
from itertools import combinations

def part_1(machines: list[MachineState]) -> int:
    sum = 0
    for machine in machines:        
        for number_of_buttons_to_press in range(1, len(machine.buttons) + 1):
            buttons_to_press = combinations(machine.buttons, number_of_buttons_to_press)

            answer_found = False
            for button_combination in buttons_to_press:
                final_state = press_buttons(machine, button_combination)
                if final_state == machine.desired_state:
                    sum += number_of_buttons_to_press
                    answer_found = True
                    break
            
            if answer_found:
                break   
    return sum

def press_buttons(machine: MachineState, buttons_to_press ) -> list[bool]:
    state = [False] * len(machine.desired_state)
    for button in buttons_to_press:
        for light in button:
            state[light] = not state[light]

    return state

def part_2(machines: list[MachineState]) -> int:
    total_cost = 0
    for machine in machines:
        model = pulp.LpProblem("MinimizeButtonCost", pulp.LpMinimize)
        
        button_vars = []
        for i, button in enumerate(machine.buttons):
            var = pulp.LpVariable(f'button_{i}', cat='Integer', lowBound=0)
            button_vars.append(var)

        model += pulp.lpSum(button_vars)

        for light_index in range(len(machine.desired_state)):
            model += (pulp.lpSum([button_vars[i] for i, button in enumerate(machine.buttons) if light_index in button]) == machine.joltages[light_index])

        model.solve(pulp.PULP_CBC_CMD(msg=False))
        
        total_cost += pulp.value(model.objective)

    return total_cost