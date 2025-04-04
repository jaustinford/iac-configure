"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("reboot-elysianskies-onprem-docker", "up --detach")
wrappers.compose_logs("reboot-elysianskies-onprem-docker")
wrappers.compose_down("reboot-elysianskies-onprem-docker")

input("\nPress [enter] to continue... ")
