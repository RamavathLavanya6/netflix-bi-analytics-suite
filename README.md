# Netflix Ultimate BI Analytics Suite 📺

[![Live App](https://img.shields.io/badge/Live-Demo-red?style=for-the-badge&logo=streamlit)](https://netflix-bi-analytics-suite-bpplgi7vs32sop2frnffuj.streamlit.app/)

A premium, enterprise-grade Business Intelligence and Data Analytics dashboard for exploring Netflix catalog data, built using **Streamlit** and **Plotly**.

This suite enables administrators and business analysts to manipulate worldwide catalog distributions, analyze ingest goals, track operational trends over time, partition content structural hierarchies, and trace global GIS spatial patterns.

## Features

1. **Dashboard Controls**: Multiselect territorial focus and segment focus between Movies and TV Shows.
2. **Key Performance Indicators (KPIs)**: Dynamic metrics displaying catalog volume, active market zones, categories, and inventory ingest targets vs. actuals via standard gauge metrics.
3. **Operational Trends**: Bars and Cumulative Database Scale combo charting alongside area-based ribbon charts showing territory rank variations.
4. **Hierarchies and Pipelines**: Interactive donut distribution charts, nested multi-dimensional treemaps, and intake/outflow waterfall variance pacing.
5. **Relationships and AI-Engineered Clustering**: Release vs. intake year bubble coordinate spaces, dynamic functional decomposition trees, and style-gradient pivots.
6. **Geographic Footprints**: Global GIS choropleths and spatial bubble mapping using coordinates.

---

## Installation & Setup

Ensure Python is installed on your system, then follow the instructions below to run the application locally.

### 1. Clone the Repository
```bash
git clone https://github.com/RamavathLavanya6/netflix-bi-analytics-suite.git
cd netflix-bi-analytics-suite
```

### 2. Install Dependencies
Install all required libraries using the package manager:
```bash
pip install -r requirements.txt
```

### 3. Run the Dashboard
Start the Streamlit local development server:
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## Data Pipeline & Cleaning

The analytics suite loads Netflix titles dynamically.
- **Production Mode**: Attempts to parse the local download database (`C:\Users\lavanya ramavath\Downloads\archive.zip`).
- **Resilient Fallback**: Instantly falls back to an AI-simulated dataset if files are missing, ensuring 100% operational uptime.
- Duplicates are systematically pruned, null records filled, and temporal strings converted to analytical pandas datetimes automatically.

## Technology Stack

- **Streamlit** - High-speed interactive web runtime
- **Plotly.py** - Dynamic charting engines and spatial maps
- **Pandas & NumPy** - Data preparation, pipeline scaling, and matrix pivots
