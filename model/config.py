from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    """Top level configurations of how LeGit should behave, regardless of matched scopes and rules"""

    ...  # TODO
