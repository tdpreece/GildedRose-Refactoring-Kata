# -*- coding: utf-8 -*-
from copy import deepcopy
import unittest

from approvals import ApprovalTest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        # need to wrap items in another list becuase approvals
        # anticipates dealing with a function with a large number
        # of inputs.
        approval_test = ApprovalTest(get_updated_items, item_equal)
        approval_test.record([items])
        approval_test.verify()


def item_equal(items_1, items_2):
    assert all(
        i[0].name == i[1].name and i[0].sell_in == i[1].sell_in and i[0].quality == i[1].quality
        for i in zip(items_1, items_2)
    ) is True


def get_updated_items(items):
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return gilded_rose.items



if __name__ == '__main__':
    unittest.main()
