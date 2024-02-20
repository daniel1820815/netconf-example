'''Python script to push XML configuration payload to devices via NETCONF'''
import logging
from ncclient import manager

logging.basicConfig(level=logging.DEBUG)

# List of devices IOSXE devices
iosxe_devices = ["192.168.255.51", "192.168.255.52", "192.168.255.53"]

# List of NX-OS device configurations
nxos_configs = ["native_interfaces", "openconfig_interfaces", "openconfig_bgp"]

# Loop through the devices and connect to it
for device in iosxe_devices:
    router = manager.connect(
        host=device,
        username="expert",
        password="1234QWer!",
        hostkey_verify=False
        )

    # For the NX-OS device
    if device == "192.168.255.53":
        # Loop through the NXOS configs and apply it
        for config in nxos_configs:
            with open(f"nxos_{config}.xml", encoding="utf-8") as file:
                payload = file.read()
            router.edit_config(payload, target="running")
    # For all other devices
    else:
        with open(f"{device}.xml", encoding="utf-8") as file:
            payload = file.read()
        router.edit_config(payload, target="running")
