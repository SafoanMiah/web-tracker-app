import streamlit as st
import pandas as pd
import plotly.express as px
from data_handler import load_data, save_data
from ui_components import sidebar_ui, display_data_frame, display_leaderboard

# Initialize our data in session state
if 'df' not in st.session_state:
    st.session_state.df = load_data()

# Page title and introduction
st.title("📊 Progress Tracker")

# Sidebar for data management
sidebar_ui()

# Main content area
df = st.session_state.df

# Show the data if there's something to display
if not df.empty:
    display_data_frame(df)
    display_leaderboard(df)
else:
    st.info("Looks like there's no data yet. Use the sidebar to add names and metrics to get started!")
