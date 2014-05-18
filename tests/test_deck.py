#!/usr/bin/env python

import unittest
import sys
sys.path.append('..')
import deck

class Test(unittest.TestCase):
    def setUp(self):
        mydeck = deck.Deck()
        pass

    def test_deck_count(self):
        mydeck = deck.Deck()
        self.assertEqual(51, mydeck.count())

    def test_assert_false(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
