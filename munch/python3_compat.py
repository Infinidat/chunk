from six import u, iteritems, iterkeys # pylint: disable=unused-import
try:
    from collection.abc import Mapping  # pylint: disable=unused-import
except ImportError:
    # Legacy Python
    from collections import Mapping  # pylint: disable=unused-import
