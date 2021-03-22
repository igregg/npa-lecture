import textfsm

raw_text = open('show_interface.log', mode='r', encoding='utf-8').read()
template = open('cisco_ios_show_interfaces.textfsm')

re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_text)

print(re_table.header)
print(fsm_results)
