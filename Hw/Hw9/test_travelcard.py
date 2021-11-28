import unittest
import travel_card


class TravelCardTest(unittest.TestCase):
    def setUp(self):
        self.card_a = travel_card.Throwaway()
        self.card_b = travel_card.CreditCard(1200)
        self.card_c = travel_card.CreditTimingCard(320)
        self.card_d = travel_card.CreditCard(12)

    def test_throwaway_card(self):
        self.assertTrue(self.card_a.used_card, 1)

    def test_credit_card(self):
        self.card_b.using_card()
        self.card_b.using_card()
        self.assertTrue(self.card_b.charge, 1100)

    def test_credit_timing_card(self):
        self.card_c.using_card()
        self.card_c.using_card()
        self.card_c.using_card()
        self.assertTrue(self.card_c.used_card, 3)

    def test_charge_credit_cart(self):
        self.card_b.recharge(100)
        self.assertTrue(self.card_b.charge, 1300)

    def test_charge_credit_timing_card(self):
        self.card_c.recharge(1230)
        self.assertTrue(self.card_c.charge, 120)

    def test_card_d(self):
        self.assertEqual(self.card_d.using_card(), None)

    def test_negative_charge(self):
        cd = travel_card.CreditCard(0)
        self.assertEqual(cd.charge, 0)

    def test_not_integer(self):
        cd = travel_card.CreditCard("abc")
        self.assertEqual(cd.charge, 0)

    def test_recharge_neg(self):
        self.card_b.recharge(-120)
        self.assertEqual(self.card_b.charge, 1200)

    def test_recharge_str(self):
        self.card_c.recharge("abc")
        self.assertEqual(self.card_c.charge, 320)


if __name__ == "__main__":
    unittest.main()
