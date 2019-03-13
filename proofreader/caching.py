#!/bin/env python

#######################################################################
# Copyright (C) 2019 Julian Dosch
#
# This file is part of ProofReader.
#
#  ProofReader is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ProofReader is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with ProofReader.  If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################

import os
from pickle import load, dump

class Cache:
    _cachedict = {}
#    with open(infile, 'rb') as infile:
#        _cachedict = pickle.load(infile)
#    _cachedict = p    with open(outfile, 'wb'):
#        pickle.dump(_cachedict, outfile, protocol=2)
    _dir_path = os.path.dirname(os.path.realpath(__file__)).split('/')
    _dir_path = "/".join(_dir_path[:-1]) + "/.cache"

    def __init__(self):
        self._read_cache()

    def __call__(self, query):
        pass

    def write_cache(self):
        outfile = open(self._dir_path + "/index", "wb")
        dump(self._cachedict, outfile, protocol=2)
        outfile.close()

    def _read_cache(self):
        if os.path.exists(self._dir_path + "/index"):
            infile = open(self._dir_path + "/index", "rb")
            self._cachedict = load(infile)
            infile.close()
