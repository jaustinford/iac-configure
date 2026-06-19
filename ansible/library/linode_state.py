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

    return json.loads(http_return.text)

def api_find_instance(token: str, label_prefix: str):
    """
    Return the ID for an instance
    fitting the 'label_prefix'.
    """

    found_instance = {}

    all_instances = api_get(
        token,
        "instances"
    )

    for instance in all_instances["data"]:
        if instance["label"].startswith(label_prefix):
            found_instance = instance

    return str(found_instance["id"])

def api_get_instance_status(token: str, instance_id: str):
    """
    Use API data to and query the
    instance status.
    """

    instance_info = {"status": ""}

    while not instance_info["status"]:
        instance_info = api_get(
            token,
            "instances/" + instance_id
        )

    return instance_info["status"]

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
        "label_prefix": {
            "type": "str",
            "required": True
        },
        "state": {
            "type": "str",
            "required": True
        }
    }

    module = AnsibleModule(argument_spec=module_args)

    arg_token        = module.params["token"]
    arg_label_prefix = module.params["label_prefix"]
    arg_state        = module.params["state"]

    found_instance_id = api_find_instance(
        arg_token,
        arg_label_prefix
    )

    if arg_state == "started":
        execute_return = api_post(
            arg_token,
            "instances/" + found_instance_id + "/boot"
        )

        while api_get_instance_status(arg_token, found_instance_id) != "running":
            time.sleep(1)

    elif arg_state == "stopped":
        execute_return = api_post(
            arg_token,
            "instances/" + found_instance_id + "/shutdown"
        )

        while api_get_instance_status(arg_token, found_instance_id) != "offline":
            time.sleep(1)

    elif arg_state == "restarted":
        execute_return = api_post(
            arg_token,
            "instances/" + found_instance_id + "/reboot"
        )

        while api_get_instance_status(arg_token, found_instance_id) != "running":
            time.sleep(1)

    execute_json = json.loads(execute_return)

    result = {
        "linode_api": execute_json,
        "changed": not bool(execute_json)
    }

    module.exit_json(**result)

if __name__ == "__main__":
    main()
