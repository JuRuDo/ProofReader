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

from urllib import parse, request

NETSPEAK_REST_BASE_URL = "http://api.netspeak.org/netspeak3/search"


class Netspeak:
    _base_query_url = "http://api.netspeak.org/netspeak3/search"

    def __call__(self, user_input):
        encoded_query = self._encode_query(user_input)
        result = self._make_request(encoded_query)
        return self._read_result(result)

    def _encode_query(self, query):
        parameters = {"query": query, "format": "text"}
        return parse.urlencode(parameters)

    def _make_request(self, encoded_query):
        return request.urlopen(self._base_query_url + "?" + encoded_query)

    def _read_result(self, result):
        return result.read().decode()
