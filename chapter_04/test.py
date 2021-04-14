import unittest
from province import Province, Producer, sample_province_data


class TestProvinceMethods(unittest.TestCase):
    def test_shortfall(self):
        asia = Province(sample_province_data())
        self.assertEqual(asia.shortfall, 5)


if __name__ == '__main__':
    unittest.main()