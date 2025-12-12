def parse(input: str) -> list[tuple[str, str]]:
    device_out_put_strings = input.strip().splitlines()
    device_outputs = []
    for device_output_string in device_out_put_strings:
        source_machine, target_machines_string = device_output_string.split(':')
        target_machines = target_machines_string.strip().split(' ')
        device_outputs.extend([(source_machine, target_machine) for target_machine in target_machines])

    return device_outputs