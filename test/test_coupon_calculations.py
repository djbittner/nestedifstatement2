import unittest
from store import coupon_calculations as coupon


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(6.89, coupon.calculate_price(5.99, 5, 10), 2)
        self.assertAlmostEqual(5.77, coupon.calculate_price(4.80, 5, 15), 2)
        self.assertAlmostEqual(6.79, coupon.calculate_price(5.99, 5, 20), 2)
        self.assertAlmostEqual(1.17, coupon.calculate_price(4.99, 10, 10), 2)
        self.assertAlmostEqual(3.38, coupon.calculate_price(7.15, 10, 15), 2)
        self.assertAlmostEqual(.78, coupon.calculate_price(3.90, 10, 20), 2)


if __name__ == '__main__':
    unittest.main()
