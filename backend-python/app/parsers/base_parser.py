from abc import ABC, abstractmethod


class BaseParser(ABC):

    @abstractmethod
    def parse(self, log: str) -> dict:
        """
        Parse a raw log and return a unified event.
        """
        pass