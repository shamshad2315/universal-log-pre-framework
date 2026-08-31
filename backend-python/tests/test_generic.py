from app.parsers.json_parser import JSONParser


def test_json_parser():
    parser = JSONParser()

    log = '{"event": "login", "user": "admin", "status": "success"}'

    result = parser.parse(log)

    assert result["parser"] == "json"
    assert result["event"] == "login"
    assert result["user"] == "admin"