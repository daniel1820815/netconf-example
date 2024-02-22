# NETCONF config example

A simple Python script using [ncclient](https://ncclient.readthedocs.io/en/latest/) library to configure two Cisco IOS-XE routers and a NX-OS switch and push configuration using NETCONF. The following configuration will be applied:

- Enable interfaces
- Add IP addresses to interfaces
- Configure BGP process with neighbor statements

The XML payloads (configuration files) were created with the help of [Cisco YANG suite](https://developer.cisco.com/yangsuite/).

The script including the XML payload was successfully tested in a Cisco Modeling Labs environment using my [DevNet Expert lab setup](https://github.com/daniel1820815/devnet-expert-cml-lab).

## Prerequisites

- Lab like my [DevNet Expert lab setup](https://github.com/daniel1820815/devnet-expert-cml-lab)
- Management access to the Cisco IOS-XE routers and NETCONF enabled
- Python ncclient library installed (see requirements.txt)

## Get started

1. Clone the repository to your machine and change into the directory:

    ```bash
    git clone https://github.com/daniel1820815/netconf-example.git
    cd netconf-example
    ```

2. It is recommended to create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install Python libraries using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:

    Before running the Python script modify the IP addresses in the script and in the XML payload files respectively according to your setup!

    ```bash
    python netconf-example.py
    ```
