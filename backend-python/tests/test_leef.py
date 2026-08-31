from app.parsers.leef_parser import LEEFParser


def test_leef_parser():
    parser = LEEFParser()

    log = (
        "LEEF:2.0|Security|Firewall|1.0|Login Failed|"
        "src=192.168.1.10|dst=10.0.0.5|usrName=admin|sev=10"
    )

    result = parser.parse(log)

    assert result["parser"] == "leef"
    assert result["event"] == "Login Failed"
    assert result["vendor"] == "Security"
    assert result["product"] == "Firewall"
    assert result["user"] == "admin"
    assert result["source_ip"] == "192.168.1.10"
    assert result["destination_ip"] == "10.0.0.5"
    assert result["severity"] == "10"