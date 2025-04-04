"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("shutdown-elysianskies-onprem-docker", "up --detach")
wrappers.compose_logs("shutdown-elysianskies-onprem-docker")
wrappers.compose_down("shutdown-elysianskies-onprem-docker")

input("\nPress [enter] to continue... ")
