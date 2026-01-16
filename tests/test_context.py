from structured_logging.context import get_context_id


def test_context_id_is_unique():
    id1 = get_context_id()
    id2 = get_context_id()
    assert id1 != id2
