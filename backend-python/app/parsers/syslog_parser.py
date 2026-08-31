import re

from .base_parser import BaseParser
from app.models.parser_response import UnifiedEvent


class SyslogParser(BaseParser):

    def parse(self, log: str) -> dict:
        try:
            log = log.strip()

            # Support optional Syslog PRI:
            # <34>Aug 30 12:00:00 server sshd: Failed login for admin
            # Aug 30 12:00:00 server sshd: Failed login for admin

            pattern = (
                r"^(?:<(\d+)>)?"
                r"(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})"
                r"\s+(\S+)\s+([^:]+):\s*(.*)$"
            )

            match = re.match(pattern, log)

            if not match:
                return {
                    "parser": "syslog",
                    "error": "Invalid Syslog format"
                }

            priority = match.group(1)
            timestamp = match.group(2)
            host = match.group(3)
            process = match.group(4)
            message = match.group(5)

            # Try to extract username from common messages
            user_match = re.search(
                r"(?:user|username)\s+([A-Za-z0-9_.-]+)",
                message,
                re.IGNORECASE
            )

            user = user_match.group(1) if user_match else None

            # Extract source IP if present
            source_ip_match = re.search(
                r"(?:src|source|src_ip)=?([0-9]{1,3}(?:\.[0-9]{1,3}){3})",
                message,
                re.IGNORECASE
            )

            source_ip = (
                source_ip_match.group(1)
                if source_ip_match
                else None
            )

            event = UnifiedEvent(
                parser="syslog",
                event=message,
                timestamp=timestamp,
                host=host,
                vendor=None,
                product=process,
                user=user,
                source_ip=source_ip,
                destination_ip=None,
                severity=None,
                data={
                    "priority": priority,
                    "process": process,
                    "message": message
                }
            )

            return event.model_dump()

        except Exception as e:
            return {
                "parser": "syslog",
                "error": "Invalid Syslog log",
                "details": str(e)
            }