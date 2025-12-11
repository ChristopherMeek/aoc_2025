from typing import NamedTuple

class MachineState(NamedTuple):
    desired_state: list[bool]
    buttons: list[int]
    joltages: list[int]

def parse(input: str) -> list[MachineState]:
    machines_string = input.strip().splitlines()

    machines = []
    for machine_str in machines_string:
        segments = machine_str.split(' ')
        desired_state_string = segments[0][1:-1]
        
        desired_state = [c == '#' for c in desired_state_string]
        
        buttons = []
        for button_str in segments[1:-1]:
            button_str = button_str[1:-1]
            button = list(map(int, button_str.split(',')))
            buttons.append(button)
        
        joltages_str = segments[-1][1:-1]
        joltages = list(map(int, joltages_str.split(',')))
        
        machines.append(MachineState(desired_state, buttons, joltages))
        
    return machines