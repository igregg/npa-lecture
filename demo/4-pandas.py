import textfsm
import pandas as pd

raw_text = open('show_interface.log', mode='r', encoding='utf-8').read()
template = open('cisco_ios_show_interfaces.textfsm')

re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_text)

intf_table = pd.DataFrame(fsm_results, columns=re_table.header)

# print data type eash column
print(intf_table.dtypes)

# filter interface has value 'up' in 'LINK_STATUS'
print(intf_table[intf_table['LINK_STATUS'] == 'up'])

intf_table = intf_table.astype({'INPUT_PACKETS': 'int64', 'OUTPUT_PACKETS': 'int64'})
# see the data type of INPUT_PACKETS, OUTPUT_PACKETS changes to int64
print(intf_table.dtypes)

# filter interface has OUTPUT_PACKETS more than 0
print(intf_table[intf_table['OUTPUT_PACKETS'] > 0])

# export to CSV
intf_table.to_csv('interfaces.csv', encoding='utf-8', index=False)
