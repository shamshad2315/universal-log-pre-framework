from .base_parser import BaseParser


class GenericParser(BaseParser):

    def parse(self, log: str) -> dict:
        try:
            return {
                "parser": "generic",
                "event": log,
                "data": {}
            }

        except Exception as e:
            return {
                "parser": "generic",
                "error": "Invalid log",
                "details": str(e)
            }