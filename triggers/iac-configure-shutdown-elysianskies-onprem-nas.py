"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("shutdown-elysianskies-onprem-nas", "up --detach")
wrappers.compose_logs("shutdown-elysianskies-onprem-nas")
wrappers.compose_down("shutdown-elysianskies-onprem-nas")

input("\nPress [enter] to continue... ")
