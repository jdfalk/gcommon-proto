#!/usr/bin/env python3
# file: sdks/python/models/model.py
# version: 1.1.0
# guid: 362d70d6-02c6-4e07-8651-99d5df9dd0d3
"""Data model definitions for the Python SDK."""
from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass, field
from typing import Any, Dict, Mapping


@dataclass(slots=True)
class ExampleModel:
    """Example data model used in sample services.

    Parameters
    ----------
    identifier:
        Unique identifier for the record.
    name:
        Human readable name associated with the model.
    created:
        Timestamp when the model was created.  Defaults to current UTC time.
    metadata:
        Optional key/value metadata attached to the model.  Keys and values must
        be strings.
    """

    identifier: str
    name: str
    created: _dt.datetime = field(default_factory=_dt.datetime.utcnow)
    metadata: Dict[str, str] = field(default_factory=dict)

    # ------------------------------------------------------------------
    def validate(self) -> None:
        """Validate the model and raise ``ValueError`` if invalid."""

        if not self.identifier:
            raise ValueError("identifier is required")
        if not self.name:
            raise ValueError("name is required")
        for key, value in self.metadata.items():
            if not isinstance(key, str) or not isinstance(value, str):
                raise ValueError("metadata keys and values must be strings")

    # ------------------------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        """Return a JSON serializable representation of the model."""

        return {
            "id": self.identifier,
            "name": self.name,
            "created": self.created.isoformat(),
            "metadata": dict(self.metadata),
        }

    # ------------------------------------------------------------------
    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ExampleModel":
        """Create a model from a mapping.

        This method is lenient and will ignore extra keys.
        """

        identifier = str(data.get("id", ""))
        name = str(data.get("name", ""))
        created_str = data.get("created")
        created = (
            _dt.datetime.fromisoformat(created_str)
            if isinstance(created_str, str)
            else _dt.datetime.utcnow()
        )
        metadata_raw = data.get("metadata", {})
        metadata: Dict[str, str] = {
            str(k): str(v) for k, v in dict(metadata_raw).items()
        }
        model = cls(identifier, name, created, metadata)
        model.validate()
        return model


__all__ = ["ExampleModel"]
