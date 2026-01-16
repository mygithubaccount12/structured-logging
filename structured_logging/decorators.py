from functools import wraps
from typing import Callable, Any, Optional
from .core import log_event
from .context import get_context_id
from .enums import OperationStage


def instrument_operation(operation_name: str, service: str = "default"):
    """
    Decorator for high-level operations.
    Automatically generates a context_id and logs start/end events.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            context_id = get_context_id()

            # Start event
            log_event(
                service=service,
                operation=operation_name,
                stage=OperationStage.START.value,
                context_id=context_id,
            )

            result = func(*args, **kwargs)

            # End event
            log_event(
                service=service,
                operation=operation_name,
                stage=OperationStage.END.value,
                context_id=context_id,
                payload={"result": result} if result is not None else None,
            )

            return result
        return wrapper
    return decorator


def instrument_stage(stage_name: str, service: str = "default", operation: Optional[str] = None):
    """
    Decorator for stages within an operation.
    Reuses an existing context_id.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            context_id = get_context_id()

            log_event(
                service=service,
                operation=operation or func.__name__,
                stage=stage_name,
                context_id=context_id,
            )

            return func(*args, **kwargs)
        return wrapper
    return decorator


def instrument_function(service: str = "default"):
    """
    Decorator for simple functions where only function name matters.
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            context_id = get_context_id()

            log_event(
                service=service,
                operation=func.__name__,
                stage=OperationStage.CALL.value,
                context_id=context_id,
            )

            return func(*args, **kwargs)
        return wrapper
    return decorator
