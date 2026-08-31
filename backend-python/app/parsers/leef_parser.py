from .base_parser import BaseParser
from app.models.parser_response import UnifiedEvent


class LEEFParser(BaseParser):

    def parse(self, log: str) -> dict:
        try:
            parts = log.split("|")

            # LEEF format validation
            if len(parts) < 5 or not parts[0].startswith("LEEF:"):
                return {
                    "parser": "leef",
                    "error": "Invalid LEEF format"
                }

            # LEEF header
            version = parts[0].replace("LEEF:", "")
            vendor = parts[1]
            product = parts[2]
            product_version = parts[3]
            event = parts[4]

            # Parse remaining key=value fields
            data = {}

            for item in parts[5:]:
                if "=" in item:
                    key, value = item.split("=", 1)
                    data[key] = value

            unified_event = UnifiedEvent(
                parser="leef",
                event=event,
                timestamp=None,
                host=data.get("devTime"),
                vendor=vendor,
                product=product,
                user=data.get("usrName"),
                source_ip=data.get("src"),
                destination_ip=data.get("dst"),
                severity=data.get("sev"),
                data={
                    "version": version,
                    "product_version": product_version,
                    **data
                }
            )

            return unified_event.model_dump()

        except Exception as e:
            return {
                "parser": "leef",
                "error": "Invalid LEEF log",
                "details": str(e)
            }