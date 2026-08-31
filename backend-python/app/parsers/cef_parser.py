from app.models.parser_response import UnifiedEvent
from app.parsers.base_parser import BaseParser


class CEFParser(BaseParser):

    def parse(self, log: str) -> dict:
        try:
            parts = log.split("|")

            if len(parts) < 8 or not parts[0].startswith("CEF:"):
                return {
                    "parser": "cef",
                    "error": "Invalid CEF format"
                }

            header = parts[0].split(":", 1)[1]
            extension = "|".join(parts[7:])

            header_parts = parts[:7]

            version = header
            device_vendor = header_parts[1]
            device_product = header_parts[2]
            device_version = header_parts[3]
            signature_id = header_parts[4]
            name = header_parts[5]
            severity = header_parts[6]

            fields = {}

            for item in extension.split():
                if "=" in item:
                    key, value = item.split("=", 1)
                    fields[key] = value

            unified_event = UnifiedEvent(
                parser="cef",
                event=name,
                timestamp=fields.get("rt"),
                host=fields.get("dhost"),
                vendor=device_vendor,
                product=device_product,
                user=fields.get("suser"),
                source_ip=fields.get("src"),
                destination_ip=fields.get("dst"),
                severity=severity,
                data={
                    "version": version,
                    "device_version": device_version,
                    "signature_id": signature_id,
                    **fields
                }
            )

            return unified_event.model_dump()

        except Exception as e:
            return {
                "parser": "cef",
                "error": "Invalid CEF log",
                "details": str(e)
            }