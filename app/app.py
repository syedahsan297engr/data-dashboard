import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import streamlit as st
from src.data.loader import DataLoader
from src.preprocessing.preprocessing import DataPreprocessor
from src.visualization.visualization_handler import VisualizationHandler  # Import VisualizationHandler
from src.advance_visualization.visualizer import Visualizer
import pandas as pd

# Initialize Loader, Preprocessor, ModelHandler, and VisualizationHandler
loader = DataLoader()
preprocessor = DataPreprocessor()
visualizer = VisualizationHandler()
advance_visualizer = Visualizer()  # Initialize Visualizer

st.set_page_config(page_title="Data Processing App", layout="wide")

st.title("Data Processing, Visualization, and Analysis App")

# Tabs for Dataset and Preprocessing
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dataset Viewer", "🛠️ Preprocessing", "📈 Visualizations", "📈 Advance Visualizations"])

### **Tab 1: Dataset Viewer**
with tab1:
    st.sidebar.header("Available Datasets")
    

### **Tab 2: Preprocessing**
with tab2:
    st.subheader("Preprocessing Dataset")

### **Tab 3: Visualizations**
with tab3:
    st.subheader("Data Visualizations")

# Advanced Data Visualizations
with tab4:
    st.subheader("Advanced Data Visualizations")