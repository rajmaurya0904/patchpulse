"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import patchpulse


def test_version_is_set() -> None:
    assert patchpulse.__version__
