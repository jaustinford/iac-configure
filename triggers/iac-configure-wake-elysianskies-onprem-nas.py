"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("wake-elysianskies-onprem-nas", "up --detach")
wrappers.compose_logs("wake-elysianskies-onprem-nas")
wrappers.compose_down("wake-elysianskies-onprem-nas")

input("\nPress [enter] to continue... ")
