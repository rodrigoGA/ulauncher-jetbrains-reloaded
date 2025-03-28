""" Contains IdeData class """
from typing import List


# pylint: disable=too-few-public-methods
class IdeData:
    """ Class describing ide options"""
    name: str
    config_prefix: str
    launcher_prefixes: List[str]

    def __init__(self, name: str, config_prefix: str, launcher_prefixes: List[str]) -> None:
        super().__init__()
        self.name = name
        self.config_prefix = config_prefix
        self.launcher_prefixes = launcher_prefixes
