import streamlit as st
from data_handler import load_data
from ui_components import sidebar_ui, display_data_frame, display_chart, display_analytics, customize_dashboard

# Load data into session state if not already loaded
if 'df' not in st.session_state:
    st.session_state.df = load_data()

# Set the title of the app
st.title("📊 Progress Tracker")

# Display the sidebar for managing data
sidebar_ui()

# Access the data frame from session state
df = st.session_state.df

# Allow users to customize which parts of the dashboard to view
show_data_frame, show_analytics = customize_dashboard()

# Display the main content if there's data available
if not df.empty:
    if show_data_frame:
        display_data_frame(df)
    
    # Let users choose which type of chart to display
    chart_type = st.selectbox(
        "Select Chart Type",
        ('Bar Chart', 'Pie Chart', 'Line Chart')
    )
    
    display_chart(df, chart_type)

    if show_analytics:
        display_analytics(df)
else:
    st.info("Looks like there's no data yet. Use the sidebar to add names and metrics to get started!")
