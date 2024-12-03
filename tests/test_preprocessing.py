import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import unittest
import pandas as pd
from src.preprocessing.preprocessing import DataPreprocessor

class TestDataPreprocessor(unittest.TestCase):
    def setUp(self):
        self.preprocessor = DataPreprocessor()
        self.sample_data = pd.DataFrame({
            "A": [1, 2, None, 4],
            "B": ["cat", "dog", "cat", "dog"],
            "C": [10, 20, 30, 40]
        })

    def test_handle_missing_values_drop(self):
        processed = self.preprocessor.handle_missing_values(self.sample_data, method='drop')
        self.assertEqual(len(processed), 3)

    def test_handle_missing_values_fill(self):
        processed = self.preprocessor.handle_missing_values(self.sample_data, method='fill', fill_value=0)
        self.assertEqual(processed["A"].iloc[2], 0)

    def test_remove_duplicates(self):
      data_with_duplicates = pd.concat([self.sample_data, self.sample_data.iloc[[0]]], ignore_index=True)
      processed = self.preprocessor.remove_duplicates(data_with_duplicates)
      self.assertEqual(len(processed), len(self.sample_data))

    def test_normalize_column(self):
        processed = self.preprocessor.normalize_column(self.sample_data, "C")
        self.assertAlmostEqual(processed["C"].max(), 1.0)

    def test_encode_categorical(self):
        processed = self.preprocessor.encode_categorical(self.sample_data, ["B"])
        self.assertTrue(processed["B"].isin([0, 1]).all())

    def test_split_data(self):
        train, test = self.preprocessor.split_data(self.sample_data, test_size=0.25)
        self.assertEqual(len(test), 1)
        self.assertEqual(len(train), 3)

if __name__ == "__main__":
    unittest.main()
