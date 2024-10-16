import streamlit as st
import pandas as pd
import plotly.express as px
from data_handler import save_data

def sidebar_ui():
    st.sidebar.header("Manage Your Data")

    # Adding a new entity (person, team, etc.)
    st.sidebar.subheader("Add New")
    new_name = st.sidebar.text_input("Index Name")
    if st.sidebar.button("Add"):
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

    # Adding a new metric (goal, task, etc.)
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

def display_data_frame(df):
    st.subheader("📝 Data Frame")

    # Editable table for easy updates
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

def display_leaderboard(df):
    st.subheader("🏅 Leaderboard")

    # Convert metric columns to numbers, just in case
    score_cols = [col for col in df.columns if col != 'Name']
    for col in score_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Calculate total scores
    df['Total Score'] = df[score_cols].sum(axis=1)
    leaderboard = df[['Name', 'Total Score']].sort_values(by='Total Score', ascending=False)

    st.table(leaderboard)

    # Show a chart of the results
    st.subheader("📊 How's Everyone Doing?")
    fig = px.bar(leaderboard, x='Name', y='Total Score', title='Total Scores')
    st.plotly_chart(fig, use_container_width=True)
