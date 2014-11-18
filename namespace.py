#!/usr/bin/env python

import collections


class Namespace(collections.defaultdict):

    def __init__(self):
        collections.defaultdict.__init__(self, Namespace)

    __getattr__ = collections.defaultdict.__getitem__
    __setattr__ = collections.defaultdict.__setitem__
