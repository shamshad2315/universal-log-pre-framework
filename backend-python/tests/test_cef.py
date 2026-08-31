from app.parsers.cef_parser import CEFParser


def test_cef_parser():
    parser = CEFParser()

    log = (
        "CEF:0|Security|Firewall|2.0|100|Login Failed|10|"
        "src=192.168.1.10 dst=10.0.0.5 suser=admin"
    )

    result = parser.parse(log)

    assert result["parser"] == "cef"
    assert result["event"] == "Login Failed"
    assert result["vendor"] == "Security"
    assert result["product"] == "Firewall"
    assert result["user"] == "admin"
    assert result["source_ip"] == "192.168.1.10"
    assert result["destination_ip"] == "10.0.0.5"
    assert result["severity"] == "10"