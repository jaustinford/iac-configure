"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("site", "up --detach")
wrappers.compose_logs("site")
wrappers.compose_down("site")

input("\nPress [enter] to continue... ")
