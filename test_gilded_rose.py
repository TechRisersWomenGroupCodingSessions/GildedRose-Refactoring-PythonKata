# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
Item(name="+5 Dexterity Vest", sell_in=10, quality=20),

class GildedRoseTest(unittest.TestCase):


    def test_dexterity_vest_regular_degradation(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)

        for i in range(0,3):
            gilded_rose.update_quality()

            self.assertEqual("+5 Dexterity Vest", items[0].name)
            self.assertEqual(9-i, items[0].sell_in)
            self.assertEqual(19-i, items[0].quality)

    def test_dexterity_vest_post_sell_in_degradation(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=2, quality=20)]
        gilded_rose = GildedRose(items)

        for i in range(0,2):
            gilded_rose.update_quality()

        gilded_rose.update_quality() # day -1

        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(16, items[0].quality)

    def test_dexterity_vest_quality_not_below_zero(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=2, quality=20)]
        gilded_rose = GildedRose(items)

        for i in range(0,30):
            gilded_rose.update_quality()

        self.assertTrue(items[0].quality == 0)

    def test_aged_brie(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)

        for i in range(0,2):
            gilded_rose.update_quality()

            self.assertEqual("Aged Brie", items[0].name)
            self.assertEqual(1-i, items[0].sell_in)
            self.assertEqual(1+i, items[0].quality)

    def test_aged_brie_after_sellIn(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)

        for i in range(0,2):
            gilded_rose.update_quality()

        for i in range(1,3):
            gilded_rose.update_quality()

            self.assertEqual("Aged Brie", items[0].name)
            self.assertEqual(-i, items[0].sell_in)
            self.assertEqual(2 +(i*2), items[0].quality)

if __name__ == '__main__':
    unittest.main()

