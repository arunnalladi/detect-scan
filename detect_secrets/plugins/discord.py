"""
This plugin searches for Discord Bot Token
"""
import re

from .base import RegexBasedDetector


class DiscordBotTokenDetector(RegexBasedDetector):
    """Scans for Discord Bot token."""
    secret_type = 'Discord Bot Token'

    denylist = [
        # Discord Bot Token ([M|N|O]XXXXXXXXXXXXXXXXXXXXXXX[XX].XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXX)
        # Reference: https://discord.com/developers/docs/reference#authentication
        # Also see: https://github.com/Yelp/detect-secrets/issues/627
        re.compile(r'[MNO][a-zA-Z\d_-]{23,25}\.[a-zA-Z\d_-]{6}\.[a-zA-Z\d_-]{27}'),
    ]
