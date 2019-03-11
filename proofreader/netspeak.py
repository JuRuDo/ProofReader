#!/bin/env python

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
