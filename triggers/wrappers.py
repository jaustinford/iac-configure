"""
Wrap common Docker Compose
commands for quick execution.
"""

import os

FILE_PATH   = os.path.abspath(__file__)
DIR_FILE    = os.path.dirname(FILE_PATH)
DIR_PROJECT = os.path.dirname(DIR_FILE)

def compose_up(compose_profile: str, compose_method: str):
    """
    Execute Docker Compose to deploy
    profile service.
    """

    if compose_method == "build":
        os.environ["DOCKER_BUILDKIT"] = "1"

    os.system(
        "docker compose" + \
            " --project-directory=" + DIR_PROJECT + \
            " --profile=" + compose_profile + \
            " " + compose_method
    )

def compose_down(compose_profile: str):
    """
    Execute Docker Compose to destroy
    profile service.
    """

    os.system(
        "docker compose" + \
            " --project-directory=" + DIR_PROJECT + \
            " --profile=" + compose_profile + \
            " down"
    )

def compose_exec(compose_service: str, compose_command: str):
    """
    Execute Docker Compose command
    inside existing container.
    """

    os.system(
        "docker compose" + \
            " --project-directory=" + DIR_PROJECT + \
            " exec " + compose_service + " " + compose_command
    )

def compose_logs(compose_profile: str):
    """
    Tail the logs of a running
    container.
    """

    os.system(
        "docker compose" + \
            " --project-directory=" + DIR_PROJECT + \
            " --profile=" + compose_profile + \
            " logs \
                --follow \
                --timestamps"
    )
