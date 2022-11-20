"""AbstractPersonDetector
AbstractPersonDetector
Usage:
    from abstract_person_detector import AbstractPersonDetector
"""

import abc


class AbstractPersonDetector(abc.ABC):
    """AbstractPersonDetector
    AbstractPersonDetector
    Attributes:
        None
    """
    @abc.abstractmethod
    def from_pretrained(self,):
        """from_pretrained
        To be implemented by subclasses.
        Args:
            None
        Returns:
            None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def detect(self,):
        """detect person
        Detect person.
        Args:
            None
        Returns:
            None
        """
        raise NotImplementedError
