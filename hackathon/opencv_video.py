"""OpencvVideo
Implement OpencvVideo.
Usage:
    from hackathon import OpencvVideo
"""

import typing

import cv2

import hackathon


class OpencvVideo(hackathon.AbstractVideo):
    """Implement OpencvVideo
    Implement OpencvVideo.
    Attributes:
        None
    """
    def __init__(self, source: typing.Union[int, str] = 0) -> None:
        """Construct OpencvVideo.
        Construct OpencvVideo.

        Args:
            source: Video source
        """
        self.source: typing.Union[int, str] = source
        self.video: cv2.VideoCapture = cv2.VideoCapture(source,)

    def get_frame(self):
        """Implement get_frame
        Implement get_frame.
        Args:
            None
        Returns:
            None
        """
        return self.video.read()[-1]
