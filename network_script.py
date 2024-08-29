import logging
from netmiko import ConnectHandler
from netmiko.cisco import CiscoIosBase,CiscoIosSSH

device_list = ("10.0.100.105") #This will be a list of devices once POC is done.

def config():
    
    connectionSSH = CiscoIosSSH(ip=device_list,username='netguys', password='4aHB%9LuR7')
    # connection = ConnectHandler(**test_switch)
    config_bpdugaurd = ["interface range g0/2","spanning-tree portfast", "no switchport voice vlan 722"]
    connectionSSH .send_config_set(config_bpdugaurd)
    
    verify = connectionSSH .send_command("show run interface g0/2")
    
    print(verify)
    
    
    
if __name__ == "__main__":
    config()