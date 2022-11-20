"""Test AbstractPersonDetector
Test AbstractPersonDetector
Usage:
    pytest tests/test_abstract_person_detector
"""

import abc

import pytest

import hackathon


def test_abstract_person_detector_exist() -> None:
    """Test AbstractPersonDetector exist
    Test AbstractPersonDetector exist.
    Args:
        None
    Returns:
        None
    """
    assert hasattr(hackathon, "AbstractPersonDetector")


def test_abstract_person_detector_is_abstract() -> None:
    """Test AbstractPersonDetector has abstractmethod from pretrained
    Test AbstractPersonDetector has abstractmethod from pretrained.
    Args:
        None
    Returns:
        None
    """
    assert issubclass(hackathon.AbstractPersonDetector, abc.ABC)


@pytest.mark.parametrize("method", ("from_pretrained", "detect"))
def test_abstract_person_detector_has_abstract_methods(method: str) -> None:
    """Test AbstractPersonDetector has abstract method from_pretrained
    Test AbstractPersonDetector has abstract method from_pretrained.
    Args:
        None
    Returns:
        None
    """
    assert method in (
        hackathon.AbstractPersonDetector.__abstractmethods__)
