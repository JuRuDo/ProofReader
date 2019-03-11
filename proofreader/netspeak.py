#!/bin/env python

class Netspeak:
    _base_query_url = "http://api.netspeak.org/netspeak3/search"

    def __call__(self, user_input):
        encoded_query = self._encode_query(user_input)
        self._make_request(encoded_query)
        pass

    def _encode_query(self, query):
        pass

    def _make_request(self, encoded_query):
        pass