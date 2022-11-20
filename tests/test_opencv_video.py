"""Test OpencvVideo

Tests for OpencvVideo

Usage:
    pytest tests/test_opencv_video.py
"""

import cv2
import numpy

import hackathon


def test_opencv_video_exist() -> None:
    """Test OpencvVideo exist
    Assert OpencvVideo exist.
    Args:
        None
    Returns:
        None
    """
    assert hasattr(hackathon, "OpencvVideo")


def test_opencv_video_has_abstract_video_as_parent() -> None:
    """Test OpencvVideo has AbstractVideo as parent
    Test OpencvVideo has AbstractVideo as parent.
    Args:
        None
    Returns:
        None
    """
    assert issubclass(hackathon.OpencvVideo, hackathon.AbstractVideo)


def test_opencv_video_implements_abstractmethod_get_frame() -> None:
    """Test OpencvVideo implements abstractmethod get_frame
    Test OpencvVideo implement abstractmethod get_frame
    Args:
        None
    Returns:
        None
    """
    assert "get_frame" not in hackathon.OpencvVideo.__abstractmethods__


def test_opencv_video_source() -> None:
    """Test opencv video attributes
    Test opencv video attributes.
    Args:
        None
    Returns:
        None
    """
    opencv_video: hackathon.OpencvVideo = hackathon.OpencvVideo(source=0)
    assert opencv_video.source == 0
    assert isinstance(opencv_video.video, cv2.VideoCapture)


def test_opencv_video_get_frame_returns_frame() -> None:
    """Test OpencvVideo get_frame returns frame.
    Test OpencvVideo get_frame returns frame.
    Args:
        None
    Returns:
        None
    """
    opencv_video: hackathon.OpencvVideo = (
        hackathon.OpencvVideo(source="tests/test.mp4"))
    assert isinstance(opencv_video.get_frame(), numpy.ndarray)
