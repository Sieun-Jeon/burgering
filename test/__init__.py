from burgering import Burger

import unittest


class BurgerTest(unittest.TestCase):
    def setUp(self):
        self.burger = Burger()

    def test_main(self):
        self.burger.add_patty('loadfile', 0)
        self.assertIsNone(self.burger.status[0])

        self.burger.set_property({'delim': ','}, 0)
        self.assertIsNotNone(self.burger.status[0])


if __name__ == '__main__':
    unittest.main(warnings='ignore')
