from netmiko.utilities import clitable_to_dict
from textfsm import clitable


index_file = 'index'
template_dir = '/Users/thanadet.k/Projects/ntc-templates/ntc_templates/templates'

raw_text = open('show_interface.log', mode='r', encoding='utf-8').read()

cli_table = clitable.CliTable(index_file, template_dir)
attrs = {'Command': 'show interface', 'platform': 'cisco_ios'}

cli_table.ParseCmd(raw_text, attrs)

structured_data = clitable_to_dict(cli_table)
print(structured_data)
