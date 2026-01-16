import uuid

def get_context_id() -> str:
    """
    Generates a unique context ID for tracing a workflow.
    """
    return str(uuid.uuid4())
