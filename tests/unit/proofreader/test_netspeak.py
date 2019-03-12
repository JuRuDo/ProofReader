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
from unittest.mock import Mock, patch


@patch("proofreader.netspeak.request.urlopen")
class NetspeakTestCase(unittest.TestCase):
    def setUp(self):
        from proofreader.netspeak import Netspeak
        self.instance = Netspeak()

    def test_instance_has_base_query_url_attribute(self, urlopen):
        self.assertEqual(
            self.instance._base_query_url,
            "http://api.netspeak.org/netspeak3/search"
        )

    @patch("proofreader.netspeak.Netspeak._encode_query")
    def test_call_calls_encode_query(self, encode_query, urlopen):
        argument = "argument"
        self.instance(argument)
        encode_query.assert_called_once_with(argument)

    @patch("proofreader.netspeak.Netspeak._make_request")
    @patch("proofreader.netspeak.Netspeak._encode_query")
    def test_call_calls_make_request(self, encode_query, make_request, urlopen):
        argument = "argument"
        query = "one query"
        encode_query.return_value = query
        self.instance(argument)
        make_request.assert_called_once_with(query)

    @patch("proofreader.netspeak.Netspeak._read_result")
    @patch("proofreader.netspeak.Netspeak._make_request")
    @patch("proofreader.netspeak.Netspeak._encode_query")
    def test_call_calls_read_result(self, encode_query, make_request, read_result, urlopen):
        argument = "argument"
        url = "my url"
        make_request.return_value = url
        self.instance(argument)
        read_result.assert_called_once_with(url)

    @patch("proofreader.netspeak.Netspeak._read_result")
    @patch("proofreader.netspeak.Netspeak._make_request")
    @patch("proofreader.netspeak.Netspeak._encode_query")
    def test_call_returns_read_results_result(
            self, encode_query, make_request, read_result, urlopen):
        argument = "argument"
        data = "some data"
        read_result.return_value = data
        result = self.instance(argument)
        self.assertEqual(result, data)

    @patch("proofreader.netspeak.parse.urlencode")
    def test_encode_query_calls_urlencode(self, urlencode, urlopen):
        query = "my funny queRy"
        expected_arg = {"query": query, "format": "text"}
        self.instance._encode_query(query)
        urlencode.assert_called_once_with(expected_arg)

    @patch("proofreader.netspeak.parse.urlencode")
    def test_encode_query_returns_urlencodes_result(self, urlencode, urlopen):
        query = "another qUery"
        encoded_query = "the encoded query"
        urlencode.return_value = encoded_query
        result = self.instance._encode_query(query)
        self.assertEqual(encoded_query, result)

    def test_make_request_calls_urlopen(self, urlopen):
        query = "my query"
        self.instance._make_request(query)
        expected_arg = self.instance._base_query_url + "?" + query
        urlopen.assert_called_once_with(expected_arg)

    def test_make_request_returns_urlopens_result(self, urlopen):
        query = "my query"
        urlopen_result = "my result"
        urlopen.return_value = urlopen_result
        result = self.instance._make_request(query)
        self.assertEqual(result, urlopen_result)

    def test_read_result_returns_expected_data(self, urlopen):
        url = Mock()
        binary_data = Mock()
        url.read.return_value = binary_data
        data = Mock()
        binary_data.decode.return_value = data
        result = self.instance._read_result(url)
        self.assertEqual(data, result)


if __name__ == "__main__":
    unittest.main()
