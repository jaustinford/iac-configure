"""
Run Compose with script-specific arguments
and pause the screen.
"""

import wrappers

PROFILE = input("\n \033[31mprofile\033[0m : ")

print(" ")

wrappers.compose_up("builder", "build")
wrappers.compose_up(PROFILE, "up --detach")
wrappers.compose_logs(PROFILE)
wrappers.compose_down(PROFILE)

input("\nPress [enter] to continue... ")
