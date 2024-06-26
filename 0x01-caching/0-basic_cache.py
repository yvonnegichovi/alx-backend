#!/usr/bin/env python3

"""
This module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a caching system without limit """
    def put(self, key, item):
        """Does nothing"""
        pass

    def get(self, key):
        """Method """
        pass
