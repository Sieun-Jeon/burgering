import pkgutil
import patties
import importlib
import unittest

from burgering import Patty


class PattyTest(unittest.TestCase):
    def test_patty(self):
        for p in pkgutil.iter_modules(patties.__path__):
            m = importlib.import_module('patties.' + p.name)
            patty = m.patty()
            self._check_types(patty)

    def _check_types(self, patty):
        try:
            self.assertTrue(isinstance(patty, Patty))
            self.assertTrue(isinstance(patty.name, str))

            self.assertTrue(isinstance(patty.title, dict))
            self.assertIn('default', patty.title)

            self.assertTrue(isinstance(patty.input_type, tuple) or patty.input_type is None)
            self.assertTrue(isinstance(patty.output_type, tuple) or patty.input_type is None)

            self.assertTrue(isinstance(patty.dependencies, list))

        except:
            raise Exception("Error in " + patty.name)


if __name__ == '__main__':
    unittest.main(warnings='ignore')




