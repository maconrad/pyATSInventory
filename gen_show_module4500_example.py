from genie.testbed import load
from pprint import pprint
from rich import print
from rich.console import Console
from rich.table import Table
from genie import parsergen
from parser import ShowModule

console = Console()

def generate_table_hdr(table):
    """ Generates the Table Header """
    table.add_column("Module")
    table.add_column("Ports")
    table.add_column("Card Type")
    table.add_column("Model")

def get_device_details(parsed_output, table):
    """ Generates the Output table for a single device """
    
    for module_num in parsed_output['mod']:
        module = parsed_output['mod'][module_num]
        #pprint(parsed_output['mod'][module_num])
        table.add_row(
            str(module['slot']),
            str(module['port']),
            module['card_type'],
            module['model'],
        )
    
    console.print(table)

if __name__ == '__main__':
    # load the testbed file
    testbed = load('files/generated.yaml')
    # Unused
    # pprint(testbed.devices) -- TopologyDict
    # isr = testbed.devices['c1100']

    for k in testbed.devices:
        table = Table(show_header=True, header_style="bold magenta")
        generate_table_hdr(table)
        device = testbed.devices[k]
        device.connect(via = 'cli', log_stdout=False)
        #output = device.execute('show module')
        obj = ShowModule(device=device)
        parsed_output = obj.parse()
        #get_device_details(parsed_output)
        #header = ['Mod', 'Ports', 'Card Type', 'Model', 'Mode', 'Serial No.']
        #result = parsergen.oper_fill_tabular(device_output=output, device_os='iosxe', header_fields=header, index=[0])
        #pprint(result.entries)
        #parsed_output = device.parse('show module')
        #pprint(parsed_output)
        console.print(f"[bold cyan] ---------------------------------------------------------------------------")
        console.print(f"[bold cyan] {device}")
        get_device_details(parsed_output, table)
    
    console.print("[bold cyan]  ---------------------------------------Done! :thumbs_up: --------------------------")