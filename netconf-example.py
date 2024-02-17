from ncclient import manager

import logging
logging.basicConfig(level=logging.DEBUG)

# List of devices
devices = ["192.168.255.51", "192.168.255.52", "192.168.255.53"]

# Loop through the devices and connect to it
for device in devices:
    router = manager.connect(
        host=device,
        username="expert",
        password="1234QWer!",
        hostkey_verify=False
        )

    # Open config file for device as payload
    with open(f"{device}.xml") as file:
        payload = file.read()

    # Send payload to running config using edit-config
    router.edit_config(payload, target="running")
