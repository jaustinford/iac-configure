"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("secrets-decrypt", "up --detach")
wrappers.compose_logs("secrets-decrypt")
wrappers.compose_down("secrets-decrypt")

input("\nPress [enter] to continue... ")
