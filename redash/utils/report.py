"""Helpers for building paginated admin reports."""

from redash.handlers.base import paginate


def paginated_report(query_set, page, page_size, serializer):
    """Return one page of a report, serialized with the given serializer."""
    return paginate(query_set, page, page_size, serializer)
