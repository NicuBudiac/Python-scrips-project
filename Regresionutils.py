import xlrd
from pathlib import Path
from netmiko import ConnectHandler
index_id = int(input("Introduce VSAT ID: "))
vlan_id = [input("Introduce vlan(s) id (ex. 24-26):  ")]
vlan_id = vlan_id[0]
conf_type = int(input(
    "In which mode do you want to configure VSAT SW Port (for access mode write - 0 or trunk write - 1) : "))


file = Path('Wheelie.xlsx')
wb = xlrd.open_workbook(file)
sheet = wb.sheet_by_name("VSATs")



#host_ip = sheet.cell_value(rowx=index_id-1,colx=10)

#port = int(port[0])
sw_interface = sheet.cell_value(rowx=index_id-1, colx=10)
print(sw_interface)


delete_config = [f"interface {sw_interface}", "no switchport mode access", "no switchport acces vlan 24-4094",
                 "no switchport mode trunk", "no switchport trunk allow vlan 24-4094 "]

trunk_config = [f"interface {sw_interface}", "switchport mode trunk", f"switchport trunk allow vlan {vlan_id} "]

access_config = [f"interface {sw_interface}", "switchport mode access", f"switchport acces vlan  {vlan_id}"]

int_conf = [f"show running-config interface {sw_interface}"]
save_conf = ["do write"]

vsat_switch_credential = {
    "device_type": "cisco_ios",
    "ip": "172.19.2.87",
    "username": "switch",
    "password": "$SatCom$",
}

