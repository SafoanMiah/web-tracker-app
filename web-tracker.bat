@echo off
cd /d "%~dp0"
pip install streamlit pandas plotly
python3 -m streamlit run app.py
