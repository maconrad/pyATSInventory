import napalm
import sys
import os
from pprint import pprint


def main():

    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver("ios")

    username = "admin"
    password = "password"
    hostname = "10.64.110.1"


    with driver(hostname, username=username, password=password, optional_args={'port': 22}) as device:
        pprint(device.get_facts())
        pprint(device.get_environment())


if __name__ == "__main__":
    main()