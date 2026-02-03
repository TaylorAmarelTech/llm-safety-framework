"""
NOTICE: This is a sanitized version for public release.
Actual test content and exploitation techniques have been removed.
This framework provides the infrastructure for safety testing.
Users must provide their own domain-specific test content.
"""

# SPDX-FileCopyrightText: 2015 Eric Larson
#
# SPDX-License-Identifier: Apache-2.0

from .adapter import CacheControlAdapter
from .cache import DictCache


def CacheControl(
    sess,
    cache=None,
    cache_etags=True,
    serializer=None,
    heuristic=None,
    controller_class=None,
    adapter_class=None,
    cacheable_methods=None,
):

    cache = DictCache() if cache is None else cache
    adapter_class = adapter_class or CacheControlAdapter
    adapter = adapter_class(
        cache,
        cache_etags=cache_etags,
        serializer=serializer,
        heuristic=heuristic,
        controller_class=controller_class,
        cacheable_methods=cacheable_methods,
    )
    sess.mount("http://", adapter)
    sess.mount("https://", adapter)

    return sess
