"""Abstract implementation of Video

Abstract implementation of video.

Usage:
    To be subclassed.
"""

import abc


class AbstractVideo(abc.ABC):
    """AbstractVideo
    Abstract implementation of video.

    Attributes:

    """

    @abc.abstractmethod
    def get_frame(self, ):
        """get_frame
        Abstract to be implemented by videos.

        Args:
            None

        Returns:
            None
        """
