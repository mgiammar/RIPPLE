"""Additional type definitions and hints for Pydantic models."""

from teamtomo_basemodel import BaseModelTeamTomo, ExcludedTensor

# Alias so existing imports of BaseModelRIPPLE continue to work
# TODO: Change all underlying class definitions so this file can be removed.
BaseModelRIPPLE = BaseModelTeamTomo

__all__ = ["BaseModelRIPPLE", "ExcludedTensor"]
