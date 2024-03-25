'''Python script to push XML configuration payload to devices via NETCONF'''
from ncclient import manager
from lxml import etree
import xml.etree.ElementTree as ET

# List of devices IOSXE devices
devices = ["192.168.255.51", "192.168.255.52", "192.168.255.53"]

iosxe_native_filter = '''
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <bgp-state-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp-oper">
            <neighbors>
                <neighbor>
                    <neighbor-id/>
                    <session-state>fsm-established</session-state>
                </neighbor>
            </neighbors>
        </bgp-state-data>
    </filter>
'''

nxos_openconfig_filter = '''
    <filter>
        <network-instances xmlns="http://openconfig.net/yang/network-instance">
            <network-instance>
                <name>default</name>
                <protocols>
                    <protocol>
                        <identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP</identifier>
                        <name>bgp</name>
                        <bgp>
                            <neighbors>
                                <neighbor>
                                    <state>
                                        <session-state>ESTABLISHED</session-state>
                                    </state>
                                </neighbor>
                            </neighbors>
                        </bgp>
                    </protocol>
                </protocols>
            </network-instance>
        </network-instances>
    </filter>
'''

# Loop through the devices and connect to it
for device in devices:
    router = manager.connect(
        host=device,
        username="expert",
        password="1234QWer!",
        hostkey_verify=False
        )

    # Choose which filter to use
    if device == "192.168.255.53":
        netconf_filter = nxos_openconfig_filter
        url = '{http://openconfig.net/yang/network-instance}'
        root = 'root[0][0][1][0][2][0]'
    else:
        netconf_filter = iosxe_native_filter
        url = '{http://cisco.com/ns/yang/Cisco-IOS-XE-bgp-oper}'

    # Get BGP neighbors based on filter and print out
    response = router.get(filter=netconf_filter)
    xml_data = etree.tostring(
        response.data_ele,
        pretty_print=True
        ).decode()
    print(xml_data)
    # print(f"\nBGP neighbors for {device}:\n")

    # tree = ET.parse(xml_data)
    # root = tree.getroot()

    root = ET.fromstring(xml_data)
    print(root.tag, root.attrib, root[0][0][1][0])

    for neighbor in root[0][0][1][0][2][0].iter(f'{url}neighbor'):
        print('BGP Neighbor:', neighbor[0].text, neighbor[1][0].text)
