"""
Use Linode API to send power
cycle commands.
"""

import json
import time
import requests

from ansible.module_utils.basic import AnsibleModule

LINODE_API_DOMAIN  = "api.linode.com"
LINODE_API_VERSION = "v4"
LINODE_API_URL     = "https://" + LINODE_API_DOMAIN + "/" + LINODE_API_VERSION + "/linode"

def api_post(token: str, endpoint: str):
    """
    Execute URLs for the Linode API and
    return the text responses.
    """

    http_return = requests.post(
        LINODE_API_URL + "/" + endpoint,
        headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        timeout=10
    )

    return http_return.text

def api_get(token: str, endpoint: str):
    """
    Return API data against select
    endpoints.
    """

    http_return = requests.get(
        LINODE_API_URL + "/" + endpoint,
        headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        timeout=10
    )

    return http_return.text

def api_get_instance_status(token: str, instance_id: str):
    """
    Use API data to and query the
    instance status.
    """

    instance_info = api_get(
        token,
        "instances/" + instance_id
    )

    instance_info_json = json.loads(instance_info)

    return instance_info_json["status"]

def main():
    """
    Parse Ansible args, read object containing
    possible server selections and direct to
    selection process.
    """

    module_args = {
        "token": {
            "type": "str",
            "required": True,
        },
        "id": {
            "type": "str",
            "required": True
        },
        "state": {
            "type": "str",
            "required": True
        }
    }

    module = AnsibleModule(argument_spec=module_args)

    arg_token = module.params["token"]
    arg_id    = module.params["id"]
    arg_state = module.params["state"]

    if arg_state == "started":
        execute_return = api_post(
            arg_token,
            "instances/" + arg_id + "/boot"
        )

        while api_get_instance_status(arg_token, arg_id) != "running":
            time.sleep(1)

    elif arg_state == "stopped":
        execute_return = api_post(
            arg_token,
            "instances/" + arg_id + "/shutdown"
        )

    execute_json = json.loads(execute_return)

    result = {
        "linode_api": execute_json,
        "changed": not bool(execute_json)
    }

    module.exit_json(**result)

if __name__ == "__main__":
    main()
