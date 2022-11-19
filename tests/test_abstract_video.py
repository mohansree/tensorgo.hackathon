"""_summary_
"""

import hackathon


def test_abstract_video_exist() -> None:
    """_summary_
    """
    assert hasattr(hackathon, "AbstractVideo")


def test_abstract_video_has_get_frame() -> None:
    """Test abstract video has get frame.
    Test abstract video has get frame.

    Args:
        None

    Returns:
        None

    """
    assert hasattr(hackathon.AbstractVideo, "get_frame")


def test_get_frame_is_abstract() -> None:
    """Assert get_frame is abstract
    Assert get_frame is abstract.

    Args:
        None

    Returns:
        None
    """
    assert "get_frame" in hackathon.AbstractVideo.__abstractmethods__
