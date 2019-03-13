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


import unittest
from unittest.mock import patch, Mock, MagicMock
import os


class CacheTestCase(unittest.TestCase):
    def setUp(self):
        from proofreader.caching import Cache
        self.instance = Cache()

    def test_instance_has_attribute_cachedict(self):
        assert hasattr(self.instance, "_cachedict")

    def test_instance_has_attribute_base_dir_path(self):
        argument = os.path.dirname(os.path.realpath(__file__)).split('/')
        dir_path = "/".join(argument[:-3]) + "/.cache"
        self.assertEqual(self.instance._dir_path, dir_path)

    @patch("proofreader.caching.Cache._read_cache")
    def test_init_calls_read_cache(self, read_cache):
        self.instance.__init__()
        read_cache.assert_called_once_with()

    @patch("proofreader.caching.load")
    @patch("proofreader.caching.open")
    @patch("proofreader.caching.os.path.exists")
    def test_read_cache_calls_open(self, exists, open, load):
        argument = os.path.dirname(os.path.realpath(__file__)).split('/')
        dir_path = "/".join(argument[:-3]) + "/.cache"
        exists.return_value = True
        self.instance._read_cache()
        exists.assert_called_once_with(dir_path + "/index")
        open.assert_called_once_with(dir_path + "/index", "rb")

    @patch("proofreader.caching.load")
    @patch("proofreader.caching.open")
    @patch("proofreader.caching.os.path.exists")
    def test_read_cache_calls_pickle_load(self, exists, nopen, load):
        argument = os.path.dirname(os.path.realpath(__file__)).split('/')
        dir_path = "/".join(argument[:-3]) + "/.cache"
        exists.return_value = True
        argument = MagicMock()
        nopen.return_value = argument
        self.instance._read_cache()
        load.assert_called_once_with(argument)

    @patch("proofreader.caching.open")
    def test_write_cache_calls_open(self, nopen):
        argument = os.path.dirname(os.path.realpath(__file__)).split('/')
        dir_path = "/".join(argument[:-3]) + "/.cache"
        self.instance.write_cache()
        nopen.assert_called_once_with(dir_path + "/index", "wb")

    @patch("proofreader.caching.dump")
    @patch("proofreader.caching.open")
    def test_write_cache_calls_pickle_dump(self, nopen, dump):
        argument = MagicMock()
        nopen.return_value = argument
        self.instance.write_cache()
        dump.assert_called_once_with(self.instance._cachedict, argument, protocol=2)


if __name__ == "__main__":
    unittest.main()
