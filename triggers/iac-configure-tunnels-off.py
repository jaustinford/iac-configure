"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("tunnels-off", "up --detach")
wrappers.compose_logs("tunnels-off")
wrappers.compose_down("tunnels-off")

input("\nPress [enter] to continue... ")
