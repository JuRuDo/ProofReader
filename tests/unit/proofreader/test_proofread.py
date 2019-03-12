#!/bin/env python

import unittest
from unittest.mock import patch, Mock, MagicMock


@patch("proofreader.proofread.print")
@patch("proofreader.proofread.sys.argv")
@patch("proofreader.proofread.Netspeak")
class ProofreadExe(unittest.TestCase):
    def test_main_creates_Netspeak_instance(self, Netspeak, argv, mprint):
        from proofreader.proofread import main
        main()
        Netspeak.assert_called_once_with()

    def test_main_calls_Netspeak_instance_with_first_cl_argument(self, Netspeak, argv, mprint):
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

    def test_main_calls_print(self, Netspeak, argv, mprint):
        from proofreader.proofread import main
        netspeak_instance = Mock()
        Netspeak.return_value = netspeak_instance
        query = Mock()
        netspeak_instance.return_value = query
        main()
        mprint.assert_called_once_with(query)


if __name__ == "__main__":
    unittest.main()
