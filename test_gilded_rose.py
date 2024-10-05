# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
Item(name="+5 Dexterity Vest", sell_in=10, quality=20),

class GildedRoseTest(unittest.TestCase):


    def test_dexterity_vest(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("+5 Dexterity Vest", items[0].name)

        
if __name__ == '__main__':
    unittest.main()

