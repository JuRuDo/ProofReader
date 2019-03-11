#!/bin/env python

import unittest
from unittest.mock import Mock, patch


class NetspeakTestCase(unittest.TestCase):
    def setUp(self):
        from proofreader.netspeak import Netspeak
        self.instance = Netspeak()

    def test_instance_has_base_query_url_attribute(self):
        self.assertEqual(
            self.instance._base_query_url,
            "http://api.netspeak.org/netspeak3/search"
        )

    @patch("proofreader.netspeak.Netspeak._encode_query")
    def test_call_calls_encode_query(self, encode_query):
        argument = "argument"
        self.instance(argument)
        encode_query.assert_called_once_with(argument)

    @patch("proofreader.netspeak.Netspeak._make_request")
    @patch("proofreader.netspeak.Netspeak._encode_query")
    def test_call_calls_make_request(self, encode_query, make_request):
        argument = "argument"
        query = Mock()
        encode_query.return_value = query
        self.instance(argument)
        make_request.assert_called_once_with(query)


if __name__ == "__main__":
    unittest.main()
