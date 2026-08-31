from app.parsers.syslog_parser import SyslogParser


def test_syslog_parser():
    parser = SyslogParser()

    log = "<34>Aug 30 12:00:00 server sshd: Failed login for user admin"

    result = parser.parse(log)

    assert result["parser"] == "syslog"
    assert result["event"] == "Failed login for user admin"
    assert result["timestamp"] == "Aug 30 12:00:00"
    assert result["host"] == "server"
    assert result["product"] == "sshd"
    assert result["user"] == "admin"
    assert result["data"]["priority"] == "34"