from netmiko import ConnectHandler

import os
import pandas as pd

os.environ['NET_TEXTFSM'] = '/Users/thanadet.k/Projects/ntc-templates/ntc_templates/templates'

router1 = {
    "device_type": "cisco_ios",
    "host": "10.1.0.11",
    "username": "cisco",
    "password": "cisco1234",
}
net_connect = ConnectHandler(**router1) 
output = net_connect.send_command("show interface", use_textfsm=True)

intf_table = pd.DataFrame(output)

print(intf_table.to_json(orient="records"))
