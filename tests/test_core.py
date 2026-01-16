import json
from structured_logging.core import log_event


def test_log_event_outputs_valid_json(capsys):
    log_event(
        service="test_service",
        operation="test_operation",
        stage="start",
        context_id="123",
        payload={"value": 42},
    )

    captured = capsys.readouterr().out
    event = json.loads(captured)

    assert event["service"] == "test_service"
    assert event["operation"] == "test_operation"
    assert event["stage"] == "start"
    assert event["context_id"] == "123"
    assert event["payload"] == {"value": 42}
