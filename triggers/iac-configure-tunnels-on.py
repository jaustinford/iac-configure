"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("tunnels-on", "up --detach")
wrappers.compose_logs("tunnels-on")
wrappers.compose_down("tunnels-on")

input("\nPress [enter] to continue... ")
