import json
import structured_logging.decorators as decorators


def test_instrument_operation_logs_start_and_end():
    logs = []

    # Patch the log_event used INSIDE decorators
    original = decorators.log_event

    def fake_log_event(**kwargs):
        logs.append(kwargs)
        return "{}"

    decorators.log_event = fake_log_event

    @decorators.instrument_operation("sample_op", service="test_service")
    def sample():
        return {"result": True}

    sample()

    decorators.log_event = original

    assert len(logs) == 2
    assert logs[0]["stage"] == "start"
    assert logs[1]["stage"] == "end"
