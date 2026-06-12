# Energy Monitor Dashboard ⚡

A full-stack monitoring dashboard for tracking energy consumption (electricity & gas)
across logistics depots — built with Python, SQLite, and Streamlit.

Inspired by real-world energy management software (e.g. PSI Energy Management).

---

## Screenshots

> Dashboard with KPIs, bar chart, time series, and CRUD table

![Dashboard](screenshot.png)

---

## Features

- 📊 Interactive charts (bar + line) with Plotly
- 🗄️ SQLite backend with full CRUD (Create, Read, Delete)
- 🏭 Multi-depot support (Berlin, Hamburg, Dortmund, Frankfurt, München)
- ⚡ Tracks Strom & Gas consumption over time
- 📅 Date-based filtering and time series visualization
- 🌱 Auto-seeded sample data on first launch

---

## Getting Started

**Requirements:** Python 3.10+

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/energy-monitor.git
cd energy-monitor

# Virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

App opens at `http://localhost:8501`

---

## Project Structureenergy-monitor/

├── app.py          # Streamlit frontend + charts

├── database.py     # SQLite CRUD + seed data

├── requirements.txt

├── .gitignore

└── README.md

## Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Frontend  | Streamlit               |
| Charts    | Plotly Express          |
| Backend   | Python 3.21             |
| Database  | SQLite (via sqlite3)    |
| Data      | pandas DataFrame        |

---

*Developed as a portfolio project for software engineering roles in energy & logistics.*