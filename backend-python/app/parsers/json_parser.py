import json

from .base_parser import BaseParser
from app.models.parser_response import UnifiedEvent


class JSONParser(BaseParser):

    def parse(self, log: str) -> dict:
        try:
            data = json.loads(log)

            event = UnifiedEvent(
                parser="json",
                event=data.get("event"),
                timestamp=data.get("timestamp"),
                host=data.get("host"),
                vendor=data.get("vendor"),
                product=data.get("product"),
                user=data.get("user"),
                source_ip=data.get("source_ip"),
                destination_ip=data.get("destination_ip"),
                severity=data.get("severity"),
                data=data
            )

            return event.model_dump()

        except json.JSONDecodeError as e:
            return {
                "parser": "json",
                "error": "Invalid JSON",
                "details": str(e)
            }