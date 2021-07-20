from genie.testbed import load
from pprint import pprint
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(show_header=True, header_style="bold magenta")

def generate_table_hdr():
    """ Generates the Table Header """
    table.add_column("Chassis")
    table.add_column("Hostname")
    table.add_column("Serial Number")
    table.add_column("Version")
    return table

def get_device_details(parsed_output):
    """ Generates the Output table for a single device """
    generate_table_hdr()
    
    table.add_row(
        parsed_output['version']['chassis'],
        parsed_output['version']['chassis_sn'],
        parsed_output['version']['hostname'],
        parsed_output['version']['xe_version'],
    )
    
    console.print(table)

if __name__ == '__main__':
    # load the testbed file
    testbed = load('files/my_testbed.yaml')

    # Unused
    # pprint(testbed.devices) -- TopologyDict
    # isr = testbed.devices['c1100']

    for k in testbed.devices:
        device = testbed.devices[k]
        device.connect(via = 'cli')
        parsed_output = device.parse('show version')
        get_device_details(parsed_output)
    
    console.print("[bold cyan] Done! :thumbs_up:")
    
    # Unused
    # pprint(ret)
    # Not parsed output
    # device.execute('show version')