"""
Select an ExpressVPN server either directly
or at random given select regions around
the globe.
"""

import os
import random
import yaml

from ansible.module_utils.basic import AnsibleModule

def concatentate_servers():
    """
    Read all continent server files in 'servers'
    and return a single object for all values.
    """

    evpn_servers = []

    evpn_file_dir = "/etc/ansible/library/evpn_servers"

    for evpn_file in os.listdir(evpn_file_dir):
        evpn_path = evpn_file_dir + "/" + evpn_file

        with open(evpn_path, "r", encoding="utf-8") as evpn_opened:
            evpn_loaded = yaml.safe_load(evpn_opened)

            evpn_servers.append(evpn_loaded)

    return evpn_servers

def randomize_continent(evpn_servers: list):
    """
    Select random server given no
    constraints.
    """

    random_continent_object = random.choice(evpn_servers)
    random_continent_key    = list(random_continent_object)[0]

    random_region_list   = random_continent_object[random_continent_key]
    random_region_object = random.choice(random_region_list)
    random_region_key    = list(random_region_object)[0]

    random_country_list   = random_region_object[random_region_key]
    random_country_object = random.choice(random_country_list)
    random_country_key    = list(random_country_object)[0]

    random_server_list   = random_country_object[random_country_key]
    selected_server = random.choice(random_server_list)

    return selected_server

def find_region(continent_name: str, evpn_servers: list):
    """
    Find region given 'continent_name'
    """

    for evpn_server in evpn_servers:
        if list(evpn_server)[0] == continent_name:
            random_region_list = evpn_server[continent_name]
            break

    return random_region_list

def randomize_region(continent_name: str, evpn_servers: list):
    """
    Select random server given
    'continent_name'.
    """

    random_region_list = find_region(continent_name, evpn_servers)

    random_region_object = random.choice(random_region_list)
    random_region_key    = list(random_region_object)[0]

    random_country_list   = random_region_object[random_region_key]
    random_country_object = random.choice(random_country_list)
    random_country_key    = list(random_country_object)[0]

    random_server_list   = random_country_object[random_country_key]
    selected_server = random.choice(random_server_list)

    return selected_server

def find_country(region_name: str, random_region_list: list):
    """
    Find country given 'region_name'
    """

    for region_object in random_region_list:
        if list(region_object)[0] == region_name:
            random_country_list = region_object[region_name]
            break

    return random_country_list

def randomize_country(continent_name: str, region_name: str, evpn_servers: list):
    """
    Select random server given
    'continent_name' and 'region_name'.
    """

    random_region_list  = find_region(continent_name, evpn_servers)
    random_country_list = find_country(region_name, random_region_list)

    random_country_object = random.choice(random_country_list)
    random_country_key    = list(random_country_object)[0]

    random_server_list   = random_country_object[random_country_key]
    selected_server = random.choice(random_server_list)

    return selected_server

def find_server(country_name: str, random_country_list: list):
    """
    Find server given 'country_name'
    """

    for country_object in random_country_list:
        if list(country_object)[0] == country_name:
            random_server_list = country_object[country_name]
            break

    return random_server_list

def randomize_server(continent_name: str, region_name: str, country_name: str, evpn_servers: list):
    """
    Select random server given
    'continent_name', 'region_name'
    and 'country_name'.
    """

    random_region_list  = find_region(continent_name, evpn_servers)
    random_country_list = find_country(region_name, random_region_list)
    random_server_list  = find_server(country_name, random_country_list)

    selected_server = random.choice(random_server_list)

    return selected_server

def main():
    """
    Parse Ansible args, read object containing
    possible server selections and direct to
    selection process.
    """

    module_args = {
        "continent": {
            "type": "str",
            "required": True
        },
        "region": {
            "type": "str",
            "required": False
        },
        "country": {
            "type": "str",
            "required": False
        },
        "server": {
            "type": "str",
            "required": False
        }
    }

    result = {
        "changed": False,
        "message": "ExpressVPN module didn't work."
    }

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    selector_continent = module.params["continent"]
    # selector_region    = module.params["region"]
    # selector_country   = module.params["country"]
    # selector_server    = module.params["server"]

    result["changed"] = True
    result["message"] = "ExpressVPN server has been selected."
    print(selector_continent)

    # evpn_servers = concatentate_servers()

    # if selector_continent == "random":
    #     selected_server = randomize_continent(evpn_servers)

    # else:
    #     if selector_region == "random":
    #         selected_server = randomize_region(
    #             selector_continent,
    #             evpn_servers
    #         )

    #     else:
    #         if selector_country == "random":
    #             selected_server = randomize_country(
    #                 selector_continent,
    #                 selector_region,
    #                 evpn_servers
    #             )

    #         else:
    #             if selector_server == "random":
    #                 selected_server = randomize_server(
    #                     selector_continent,
    #                     selector_region,
    #                     selector_country,
    #                     evpn_servers
    #                 )

    #             else:
    #                 selected_server = selector_server

    # if selected_server:
    #     result["changed"] = True
    #     result["message"] = "ExpressVPN server has been selected."

    # print(selected_server)

if __name__ == "__main__":
    main()
