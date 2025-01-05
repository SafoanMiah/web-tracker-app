# 📊 Web Tracker App

A simple and interactive web application to track progress using Streamlit, allowing users to add names, and metrics, and visualize the progress with a leaderboard and charts. Perfect for keeping track of individual or team achievements.

[Streamlit Web Example](https://web-tracker.streamlit.app/)

![image](https://github.com/user-attachments/assets/e5f2b0be-9674-404c-b283-51c5c174ddac)

## 🚀 Features

- Use the sidebar to add and manage entities (people, teams, etc.).
- Add new metrics (goals, tasks, etc.) for each entity.
- Easily edit data directly within the app.
- Automatically saves progress data to `progress_data.csv` for persistent storage.
- Displays a dynamic leaderboard to show progress.
- Visualizes progress data using interactive Plotly charts.
- **New:** Import data from CSV files and export current data.
- **New:** Customize dashboard views to show or hide data frames and analytics.
- **New:** Choose from multiple chart types: Bar, Pie, and Line charts.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SafoanMiah/web-tracker-app.git
   cd web-tracker-app
   ```
   
2. **Run the app**:
   ```bash
   web-tracker.bat
   ```

4. **Access the app**: Open your browser and go to `http://localhost:8501` (make sure to put in the correct port).

## 📂 Project Structure

```
progress-tracker-app/
├── app.py                # Main Streamlit app file
├── data_handler.py       # Contains data loading and saving functions
├── ui_components.py      # Contains functions for UI elements like sidebar and leaderboard
├── progress_data.csv     # Data file (auto-generated)
├── web-tracker.bat       # Bat file to run the program locally
└── README.md             # This readme file
```

## 📊 How It Works

1. **Manage Data**: Use the sidebar to add new entities (people, teams) and metrics.
2. **Edit Data**: Update progress directly in the editable table.
3. **Leaderboard**: View the leaderboard sorted by total scores.
4. **Visualize Data**: See the progress with a bar chart showing total scores.
5. **Import/Export Data**: Easily import data from CSV files and export your current data.
6. **Customize Dashboard**: Select which components of the dashboard to display, such as data frames and analytics.

## 🔧 Dependencies

- Python 3.7+
- Streamlit
- Pandas
- Plotly

## 🤝 Contributing

Feel free to fork this repository, create a new branch, and submit a pull request. Any contributions, bug fixes, or feature requests are welcome!

---

### Happy tracking! 🎯
