#!/bin/env python

import unittest


class ProofreadExe(unittest.TestCase):
    def test_main_can_be_called(self):
        from proofreader.proofread import main
        main()


if __name__ == "__main__":
    unittest.main()
