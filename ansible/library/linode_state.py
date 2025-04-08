"""
Use Linode API to send power
cycle commands.
"""

import json
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

    global_headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    http_return = requests.post(
        LINODE_API_URL + "/" + endpoint,
        headers=global_headers,
        timeout=10
    )

    return http_return.text

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

    elif arg_state == "stopped":
        execute_return = api_post(
            arg_token,
            "instances/" + arg_id + "/shutdown"
        )

    module.exit_json(
        **json.loads(execute_return)
    )

if __name__ == "__main__":
    main()
