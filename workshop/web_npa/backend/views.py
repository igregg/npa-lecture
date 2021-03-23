from django.shortcuts import render
from netmiko import ConnectHandler
import os
import pandas as pd

# Change to your ntc-template location
os.environ['NET_TEXTFSM'] = '/Users/thanadet.k/Projects/ntc-templates/ntc_templates/templates'

def connect(request):
    device = {
        "device_type": "cisco_ios",
        "host": request.POST['host'],
        "username": request.POST['username'],
        "password": request.POST['password'],
    }

    net_connect = ConnectHandler(**device)
    with net_connect as nc:
        output = nc.send_command(request.POST['cmd'], use_textfsm=True)

    intf_table = pd.DataFrame(output)

    print(intf_table.to_dict(orient="split"))

    return render(request, 'frontend/result.html', { "results": intf_table.to_dict(orient="split") })