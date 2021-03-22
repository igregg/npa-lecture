from netmiko import ConnectHandler

import os
import textfsm

os.environ['NET_TEXTFSM'] = '/Users/thanadet.k/Projects/ntc-templates/ntc_templates/templates'

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.0.11",
    "username": "cisco",
    "password": "cisco1234",
}
net_connect = ConnectHandler(**router1) 
output = net_connect.send_command("show users")

template = open('cisco_ios_show_users.textfsm')

re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(output)

print(re_table.header)
print(fsm_results)
