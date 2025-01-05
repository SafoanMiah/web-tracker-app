import streamlit as st
import pandas as pd
import plotly.express as px
from data_handler import save_data, calculate_total_scores

def sidebar_ui():
    st.sidebar.header("Manage Your Data")

    # Section to add a new index (e.g., person, team)
    st.sidebar.subheader("Add New Index")
    new_name = st.sidebar.text_input("Index Name")
    if st.sidebar.button("Add Index"):
        if new_name.strip():
            if new_name.strip() not in st.session_state.df['Name'].values:
                new_row = pd.DataFrame({'Name': [new_name.strip()]})
                st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
                save_data(st.session_state.df)
                st.sidebar.success(f'🎉 Added "{new_name.strip()}"!')
            else:
                st.sidebar.warning('🚫 That name already exists!')
        else:
            st.sidebar.error("Oops! Please enter a name.")

    st.sidebar.markdown("---")  

    # Section to add a new metric (e.g., goal, task)
    st.sidebar.subheader("Add Metric")
    new_metric = st.sidebar.text_input("Metric Column")
    if st.sidebar.button("Add Metric"):
        if new_metric.strip():
            if new_metric.strip() not in st.session_state.df.columns:
                st.session_state.df[new_metric.strip()] = ''
                save_data(st.session_state.df)
                st.sidebar.success(f'✅ Added metric "{new_metric.strip()}"!')
            else:
                st.sidebar.warning('🚫 That metric already exists!')
        else:
            st.sidebar.error("Oops! Please enter a metric name.")

    st.sidebar.markdown("---")  

    # Option to import data from a CSV file
    st.sidebar.subheader("Data Export / Import")
    
    # Option to download the current data as a CSV file
    st.sidebar.download_button(
        label="Download data as CSV",
        data=st.session_state.df.to_csv(index=False).encode('utf-8'),
        file_name='progress_data.csv',
        mime='text/csv'
    )
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        new_data = pd.read_csv(uploaded_file)
        st.session_state.df = pd.concat([st.session_state.df, new_data], ignore_index=True)
        save_data(st.session_state.df)
        st.sidebar.success("Data imported successfully!")

def display_data_frame(df):
    st.subheader("📝 Data Frame")

    # Allow users to search for specific names
    search_term = st.text_input("Search by Name")
    if search_term:
        df = df[df['Name'].str.contains(search_term, case=False, na=False)]

    # Display an editable table for the data
    try:
        edited_df = st.data_editor(
            df,
            num_rows="dynamic",
            use_container_width=True
        )
        st.session_state.df = edited_df
        save_data(st.session_state.df)
    except AttributeError:
        st.write('Looks like your version of Streamlit doesn’t support editing tables directly. Here’s what we have:')
        st.write(df)

def display_chart(df, chart_type):
    df = calculate_total_scores(df)
    leaderboard = df[['Name', 'Total Score']].sort_values(by='Total Score', ascending=False)

    if chart_type == 'Bar Chart':
        st.subheader("📊 Bar Chart")
        fig = px.bar(
            leaderboard,
            x='Name',
            y='Total Score',
            title='Total Scores',
            color='Total Score',
            color_continuous_scale=px.colors.sequential.Viridis
        )
    elif chart_type == 'Pie Chart':
        st.subheader("📈 Pie Chart")
        fig = px.pie(
            leaderboard,
            names='Name',
            values='Total Score',
            title='Score Distribution'
        )
    elif chart_type == 'Line Chart':
        st.subheader("📉 Line Chart")
        # Assuming 'Metric' is a column in the dataframe
        fig = px.line(
            df.melt(id_vars=['Name'], var_name='Metric', value_name='Score'),
            x='Metric',
            y='Score',
            color='Name',
            title='Scores by Metric'
        )

    st.plotly_chart(fig, use_container_width=True)

def display_analytics(df):
    st.subheader("📊 Data Analytics")
    st.write("### Summary Statistics")
    st.write(df.describe())

def customize_dashboard():
    st.sidebar.subheader("Customize Dashboard")
    show_data_frame = st.sidebar.checkbox("Show Data Frame", value=True)
    show_analytics = st.sidebar.checkbox("Show Analytics", value=False)
    return show_data_frame, show_analytics
