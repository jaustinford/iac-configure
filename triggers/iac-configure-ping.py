"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("ping", "up --detach")
wrappers.compose_logs("ping")
wrappers.compose_down("ping")

input("\nPress [enter] to continue... ")
