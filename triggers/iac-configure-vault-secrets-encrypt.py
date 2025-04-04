"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

wrappers.compose_up("builder", "build")
wrappers.compose_up("secrets-encrypt", "up --detach")
wrappers.compose_logs("secrets-encrypt")
wrappers.compose_down("secrets-encrypt")

input("\nPress [enter] to continue... ")
