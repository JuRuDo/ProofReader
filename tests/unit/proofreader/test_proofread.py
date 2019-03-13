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


@patch("proofreader.proofread.Cache")
@patch("proofreader.proofread.print")
@patch("proofreader.proofread.sys.argv")
@patch("proofreader.proofread.Netspeak")
class ProofreadExe(unittest.TestCase):
    def test_main_creates_Netspeak_instance(self, Netspeak, argv, mprint, Cache):
        from proofreader.proofread import main
        main()
        Netspeak.assert_called_once_with()

    def test_main_calls_Netspeak_instance_with_first_cl_argument(self, Netspeak, argv, mprint, Cache):
        from proofreader.proofread import main
        netspeak_instance = Mock()
        Netspeak.return_value = netspeak_instance
        item = MagicMock()
        d = {1: item}

        def getitem(key):
            return d[key]

        argv.__getitem__.side_effect = getitem
        main()
        netspeak_instance.assert_called_once_with(item)

    def test_main_calls_print(self, Netspeak, argv, mprint, Cache):
        from proofreader.proofread import main
        netspeak_instance = Mock()
        Netspeak.return_value = netspeak_instance
        query = Mock()
        netspeak_instance.return_value = query
        main()
        mprint.assert_called_once_with(query)

    def test_main_creates_Cache_instance(self, Netspeak, argv, mprint, Cache):
        from proofreader.proofread import main
        main()
        Cache.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
