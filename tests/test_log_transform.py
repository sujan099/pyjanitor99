import unittest
import pandas as pd
import math
from janitor.log_transform import log_transform

class TestLogTransform(unittest.TestCase):

    def test_log_transform_default_base(self):
        df = pd.DataFrame({'A': [1, math.e, math.e**2]})
        result = log_transform(df.copy(), columns=['A'])
        expected = [0, 1, 2]
        for r, e in zip(result['A'], expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_log_transform_custom_base(self):
        df = pd.DataFrame({'A': [1, 10, 100]})
        result = log_transform(df.copy(), columns=['A'], base=10)
        expected = [0, 1, 2]
        for r, e in zip(result['A'], expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_log_transform_negative(self):
        df = pd.DataFrame({'A': [-1, 2, 3]})
        with self.assertRaises(ValueError):
            log_transform(df.copy(), columns=['A'])

if __name__ == '__main__':
    unittest.main()
