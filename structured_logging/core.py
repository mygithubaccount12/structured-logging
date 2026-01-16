
import datetime
from datetime import datetime, timezone
import json
from typing import Any, Dict, Optional


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def log_event(
        *,
        service: str,
        operation: str,
        stage: str,
        context_id: str,
        user: Optional[str] = None,
        request: Optional[str] = None,
        payload: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Core structured_logging function. Enforces structured JSON logs with consistent fields.
    All decorators route through this function.

    Parameters:
        service: Name of the service or module.
        operation: High-level operation being performed.
        stage: Stage within the operation (start, end, validation, etc.).
        context_id: Unique ID for tracing a single request or workflow.
        user: Optional user identifier.
        request: Optional request identifier.
        payload: Optional additional debugging data.
    """

    event = {
        "timestamp": now_iso(),
        "service": service,
        "operation": operation,
        "stage": stage,
        "context_id": context_id,
        "user": user,
        "request": request,
        "payload": payload,
    }

    json_event = json.dumps(event)
    print(json_event)
    return json_event

