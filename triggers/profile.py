"""
Easily build and execute targeted
compose service profiles.
"""

import os
import wrappers

if os.environ.get("COMPOSE_PROFILE"):
    COMPOSE_PROFILE = os.environ.get("COMPOSE_PROFILE")

else:
    COMPOSE_PROFILE = input("\n \033[35mcompose profile\033[0m : ")

if COMPOSE_PROFILE == "site":
    if not os.environ.get("CYCLE_MODE"):
        CYCLE_MODE = input(" \033[35m     cycle mode\033[0m : ")
        os.environ["CYCLE_MODE"] = CYCLE_MODE

print(" ")

wrappers.compose_up(COMPOSE_PROFILE, "up --detach")

try:
    wrappers.compose_logs(COMPOSE_PROFILE)

except KeyboardInterrupt:
    wrappers.compose_down(COMPOSE_PROFILE)

else:
    wrappers.compose_down(COMPOSE_PROFILE)

if not os.environ.get("SKIP_PAUSE"):
    input("\nPress [enter] to continue... ")
