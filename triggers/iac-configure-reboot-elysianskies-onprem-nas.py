"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("reboot-elysianskies-onprem-nas", "up --detach")
wrappers.compose_logs("reboot-elysianskies-onprem-nas")
wrappers.compose_down("reboot-elysianskies-onprem-nas")

input("\nPress [enter] to continue... ")
