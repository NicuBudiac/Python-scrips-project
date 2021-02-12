from utils import *

if switch_id == title('Sirius'):
    net_connect = ConnectHandler(**Sirius_vsat_switch_credential)
    output = net_connect.send_config_set(delete_config)
    if conf_type == 0:
        output = net_connect.send_config_set(access_config)
        output = net_connect.send_config_set(save_conf)
        output = net_connect.send_command(f"{int_conf[0]}")
        print(output)
    elif conf_type == 1:
        output = net_connect.send_config_set(trunk_config)
        output = net_connect.send_config_set(save_conf)
        output = net_connect.send_command(f"{int_conf[0]}")
        print(output)
elif switch_id == title('Leo'):
    net_connect = ConnectHandler(**Leo_vsat_switch_credential)
    output = net_connect.send_config_set(delete_config)
    if conf_type == 0:
        output = net_connect.send_config_set(access_config)
        output = net_connect.send_config_set(save_conf)
        output = net_connect.send_command(f"{int_conf[0]}")
        print(output)
    elif conf_type == 1:
        output = net_connect.send_config_set(trunk_config)
        output = net_connect.send_config_set(save_conf)
        output = net_connect.send_command(f"{int_conf[0]}")
        print(output)
elif switch_id == title('Saturn'):
    net_connect = ConnectHandler(**Saturn_vsat_switch_credential)
    output = net_connect.send_config_set(delete_config)
    if conf_type == 0:
        output = net_connect.send_config_set(access_config)
        output = net_connect.send_config_set(save_conf)
        output = net_connect.send_command(f"{int_conf[0]}")
        print(output)
    elif conf_type == 1:
        output = net_connect.send_config_set(trunk_config)
        output = net_connect.send_config_set(save_conf)
        output = net_connect.send_command(f"{int_conf[0]}")
        print(output)

else:
    print("You choosed unsupported configuration type")
