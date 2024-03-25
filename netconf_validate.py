'''Python script to push XML configuration payload to devices via NETCONF'''
from ncclient import manager
from lxml import etree
import xml.etree.ElementTree as ET

# List of devices
devices = ["192.168.255.51", "192.168.255.52", "192.168.255.53"]


def device_connect(dev):
    '''Function to connect to the devices'''

    con = manager.connect(
        host=dev,
        username="expert",
        password="1234QWer!",
        hostkey_verify=False
        )
    return con


def get_bgp_neighbors(con, filter):
    '''Function to get BGP neighbors based on filter and return data'''

    response = con.get(filter=filter)
    data = etree.tostring(
        response.data_ele,
        pretty_print=True
        ).decode()
    # print(xml_data)
    return data


if __name__ == '__main__':

    # Loop through the devices and connect to it
    for device in devices:
        connect = device_connect(device)

        # Choose which filter to use
        if device == "192.168.255.53":
            yang_type = 'openconfig'
            url = '{http://openconfig.net/yang/network-instance}'
        else:
            yang_type = 'native'
            url = '{http://cisco.com/ns/yang/Cisco-IOS-XE-bgp-oper}'

        # Open file for NETCONF filter
        with open(f'filters/{yang_type}_bgp_neighbor_filter.xml') as file:
            netconf_filter = file.read()

        # Get XML data and read
        xml_data = get_bgp_neighbors(connect, netconf_filter)
        root = ET.fromstring(xml_data)

        # Browse through the XML tree and print all neighbors with state
        print(f'\nBGP neighbors for {device}:')
        if device == "192.168.255.53":
            for neighbor in root[0][0][1][0][2][0].iter(f'{url}neighbor'):
                address = neighbor[0].text
                state = neighbor[1][0].text
                print(f'Neighbor {address} -> {state}')
        else:
            for neighbor in root[0][0].iter(f'{url}neighbor'):
                address = neighbor[0].text
                state = neighbor[1].text
                print(f'Neighbor {address} -> {state}')
