from .json_parser import JSONParser
from .cef_parser import CEFParser
from .leef_parser import LEEFParser
from .syslog_parser import SyslogParser
from .generic_parser import GenericParser


PARSERS = {
    "json": JSONParser(),
    "cef": CEFParser(),
    "leef": LEEFParser(),
    "syslog": SyslogParser(),
    "generic": GenericParser(),
}


def get_parser(parser_type: str):
    return PARSERS.get(parser_type, PARSERS["generic"])