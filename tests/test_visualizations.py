import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import unittest
import pandas as pd
from src.visualization.visualization_handler import VisualizationHandler

class TestVisualizationHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up reusable test data and VisualizationHandler instance."""
        cls.visualizer = VisualizationHandler()
        cls.data = pd.DataFrame({
            "feature1": [1, 2, 3, 4, 5],
            "feature2": [5, 4, 3, 2, 1],
            "feature3": [2.1, 2.2, 2.3, 2.4, 2.5]
        })

    def test_create_histogram(self):
        """Test histogram generation."""
        plot_base64 = self.visualizer.create_histogram(self.data, column="feature1")
        self.assertIsInstance(plot_base64, str)
        self.assertGreater(len(plot_base64), 0)

    def test_create_scatter_plot(self):
        """Test scatter plot generation."""
        plot_base64 = self.visualizer.create_scatter_plot(self.data, x_col="feature1", y_col="feature2")
        self.assertIsInstance(plot_base64, str)
        self.assertGreater(len(plot_base64), 0)

    def test_create_correlation_heatmap(self):
        """Test correlation heatmap generation."""
        plot_base64 = self.visualizer.create_correlation_heatmap(self.data)
        self.assertIsInstance(plot_base64, str)
        self.assertGreater(len(plot_base64), 0)

if __name__ == "__main__":
    unittest.main()
