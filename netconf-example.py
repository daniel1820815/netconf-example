from ncclient import manager

import logging
logging.basicConfig(level=logging.DEBUG)

devices = ["192.168.255.51", "192.168.255.52"]

for device in devices:
    router = manager.connect(
        host=device,
        username="expert",
        password="1234QWer!",
        hostkey_verify=False
        )

    with open(f"{device}.xml") as file:
        payload = file.read()

    router.edit_config(payload, target="running")
