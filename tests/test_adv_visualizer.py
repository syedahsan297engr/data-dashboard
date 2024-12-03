import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import unittest
import pandas as pd
from src.advance_visualization.visualizer import Visualizer

class TestVisualizer(unittest.TestCase):
    def setUp(self):
        self.visualizer = Visualizer()
        self.data = pd.DataFrame({
            "A": [1, 2, 3, 4, 5],
            "B": [10, 20, 30, 40, 50],
            "C": ["cat", "dog", "cat", "dog", "cat"]
        })

    def test_create_scatter_plot(self):
        fig = self.visualizer.create_scatter_plot(self.data, x="A", y="B", color="C")
        self.assertIsNotNone(fig, "Scatter plot should not be None")

    def test_create_histogram(self):
        fig = self.visualizer.create_histogram(self.data, column="A", bins=3)
        self.assertIsNotNone(fig, "Histogram should not be None")

    def test_create_box_plot(self):
        fig = self.visualizer.create_box_plot(self.data, x="C", y="B")
        self.assertIsNotNone(fig, "Box plot should not be None")

    def test_create_heatmap(self):
        fig = self.visualizer.create_heatmap(self.data)
        self.assertIsNotNone(fig, "Heatmap should not be None")

    def test_save_figure(self):
        fig = self.visualizer.create_histogram(self.data, column="A")
        self.visualizer.save_figure(fig, filename="test_histogram.png")
        with open("test_histogram.png", "rb") as f:
            self.assertTrue(f.read(), "File should not be empty")

if __name__ == "__main__":
    unittest.main()
