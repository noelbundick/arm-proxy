from knack.help_files import helps  # pylint: disable=unused-import


helps[
    "arm-proxy"
] = """
    type: group
    short-summary: Commands to manage the local network proxy.
"""

helps[
    "arm-proxy start"
] = """
    type: command
    short-summary: Start a proxy for deploying ARM templates from your local repo.
"""
