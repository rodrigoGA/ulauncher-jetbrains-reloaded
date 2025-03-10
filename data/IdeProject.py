""" Contains project type """
from __future__ import annotations

from data.IdeKey import IdeKey


# pylint: disable=too-few-public-methods
class IdeProject:
    """ Dictionary describing project data """
    name: str
    ide: IdeKey
    path: str
    score: int
    icon: str | None

    # pylint: disable=too-many-arguments
    def __init__(self, name: str, ide: IdeKey, path: str, score: int,
                 icon: str | None = None) -> None:
        super().__init__()
        self.icon = icon
        self.score = score
        self.path = path
        self.ide = ide
        self.name = name
