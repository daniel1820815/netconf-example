# Simple NETCONF config example

A simple Python script using ncclient library to connect to two Cisco IOS-XE routers and push configuration using NETCONF. The following configuration will be applied:

- Enable interface between both Cisco IOS-XE routers
- Create two subinterfaces using dot1q tagging
- Add IP addresses to both subinterfaces
- Create a loopback interface
- Configure BGP process with neighbor statements

## Prerequisites

- Two Cisco IOS-XE routers connected together on an interface
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

    Before running the Python script modify the IP addresses in the script and in the XML payload files respectively.

    ```bash
    python netconf-example.py
    ```
