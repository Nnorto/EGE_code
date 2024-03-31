from ipaddress import *

for mask in reversed(range(0, 32+1)):
    net1 = ip_network(f'202.3.20.24/{str(mask)}', 0)
    net2 = ip_network(f'202.3.27.11/{str(mask)}', 0)
    if net1.network_address == net2.network_address :
        count = 0
        for ad in net2:
            ad2 = bin(int(ad))[2:].zfill(32)
            if ad2.count('1') % 2 == 0:
                count += 1
        print(count)
        break

for mask in reversed(range(0, 32+1)):
    net1 = ip_network(f'202.3.20.24/{str(mask)}', 0)
    net2 = ip_network(f'202.3.27.11/{str(mask)}', 0)
    if net1.network_address == net2.network_address :
        print(net2.num_addresses//2) # через сс
        break



