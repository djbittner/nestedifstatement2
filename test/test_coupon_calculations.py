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

    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(11.20, coupon.calculate_price(10.50, 5, 10), 2)
        self.assertAlmostEqual(16.45, coupon.calculate_price(16.65, 5, 15), 2)
        self.assertAlmostEqual(23, coupon.calculate_price(22.75, 5, 20), 2)
        self.assertAlmostEqual(26.22, coupon.calculate_price(29.15, 10, 10), 2)
        self.assertAlmostEqual(14.96, coupon.calculate_price(20, 10, 15), 2)
        self.assertAlmostEqual(20.16, coupon.calculate_price(24.40, 10, 20), 2)

    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(36.57, coupon.calculate_price(35, 5, 10), 2)
        self.assertAlmostEqual(47.45, coupon.calculate_price(44.40, 5, 15), 2)
        self.assertAlmostEqual(48.41, coupon.calculate_price(47.99, 5, 20), 2)
        self.assertAlmostEqual(38.17, coupon.calculate_price(41.68, 10, 10), 2)
        self.assertAlmostEqual(27.01, coupon.calculate_price(31.15, 10, 15), 2)
        self.assertAlmostEqual(33.29, coupon.calculate_price(39.88, 10, 20), 2)

    def test_price_under_over_fifty(self):
        self.assertAlmostEqual(70.31, coupon.calculate_price(78.70, 5, 10), 2)
        self.assertAlmostEqual(63.30, coupon.calculate_price(61.99, 5, 15), 2)
        self.assertAlmostEqual(79.62, coupon.calculate_price(98.89, 5, 20), 2)
        self.assertAlmostEqual(63.73, coupon.calculate_price(76.80, 10, 10), 2)
        self.assertAlmostEqual(64.42, coupon.calculate_price(81.50, 10, 15), 2)
        self.assertAlmostEqual(53.42, coupon.calculate_price(58.90, 10, 20), 2)


if __name__ == '__main__':
    unittest.main()
