"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("wake-elysianskies-onprem-docker", "up --detach")
wrappers.compose_logs("wake-elysianskies-onprem-docker")
wrappers.compose_down("wake-elysianskies-onprem-docker")

input("\nPress [enter] to continue... ")
