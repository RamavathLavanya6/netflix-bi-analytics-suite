import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# 1. PAGE CONFIGURATION & DARK THEME SETUP
# ==========================================
st.set_page_config(
    page_title="Netflix Ultimate BI Analytics Suite",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium Custom CSS Styling for an Enterprise look
st.markdown("""
    <style>
        body { background-color: #141414; color: #FFFFFF; }
        .stApp { background-color: #141414; }
        [data-testid="stSidebar"] { background-color: #1E1E1E; }
        
        /* Metric Card Styling */
        div.metric-card {
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #333333;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
        }
        
        /* Headers formatting */
        h1, h2, h3 { color: #E50914 !important; font-family: 'Helvetica Neue', Arial, sans-serif; }
        .section-header {
            border-left: 5px solid #E50914;
            padding-left: 10px;
            margin-bottom: 20px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA IMPORT & PIPELINE CLEANING
# ==========================================
@st.cache_data
def load_and_clean_dataset():
    try:
        data = pd.read_csv(r"C:\Users\lavanya ramavath\Downloads\archive.zip")
    except Exception:
        # Complete fallback dataset if file isn't found
        data = pd.DataFrame({
            'type': ['Movie', 'TV Show']*100,
            'country': ['United States', 'India', 'United Kingdom', 'Canada', 'Japan']*40,
            'rating': ['TV-MA', 'TV-14', 'R', 'PG-13', 'TV-PG']*40,
            'release_year': np.random.randint(2010, 2025, 200),
            'duration': np.random.randint(60, 180, 200),
            'listed_in': ['Dramas', 'Comedies', 'Action & Adventure', 'Documentaries', 'International']*40,
            'date_added': pd.date_range(start='2018-01-01', periods=200)
        })
    
    data.columns = data.columns.str.strip().str.lower()
    data.drop_duplicates(inplace=True)
    
    for col in ['director', 'cast', 'country', 'rating', 'listed_in']:
        if col in data.columns:
            data[col] = data[col].fillna('Unknown')
            
    if 'date_added' in data.columns:
        data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
        data['year_added'] = data['date_added'].dt.year.fillna(data['release_year']).astype(int)
    else:
        data['year_added'] = data['release_year']
        
    return data

df = load_and_clean_dataset()

# ==========================================
# 3. SIDEBAR CONTROL CENTER
# ==========================================
st.sidebar.title("🎬 Enterprise BI Control Center")
st.sidebar.markdown("Manipulate worldwide processing arrays directly.")

selected_country = st.sidebar.multiselect("Filter by Territory", options=list(df['country'].unique()), default=list(df['country'].unique())[:3])
selected_type = st.sidebar.radio("Content Segment Focus", options=["All", "Movie", "TV Show"])

# Apply filters
filtered_df = df[df['country'].isin(selected_country)]
if selected_type != "All":
    filtered_df = filtered_df[filtered_df['type'] == selected_type]

# Target for Gauge metric simulation
TARGET_INVENTORY = 1500

# ==========================================
# 4. ROW 1: KPI CARDS & GAUGES SYSTEM
# ==========================================
st.title("📺NETFLIX DATA ANALYTICS SUITE")
st.markdown("<h3 class='section-header'>Metrics, Goals & Processes</h3>", unsafe_allow_html=True)

kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns([1, 1, 1, 1.5])

with kpi_col1:
    st.markdown(f'<div class="metric-card"><h2 style="margin:0;color:#E50914!important;">{len(filtered_df)}</h2><p style="color:#808080;margin:0;">Aggregate Catalog Volume</p></div>', unsafe_allow_html=True)
with kpi_col2:
    countries_count = filtered_df['country'].nunique()
    st.markdown(f'<div class="metric-card"><h2 style="margin:0;color:#FFFFFF!important;">{countries_count}</h2><p style="color:#808080;margin:0;">Active Market Zones</p></div>', unsafe_allow_html=True)
with kpi_col3:
    genres_count = filtered_df['listed_in'].nunique()
    st.markdown(f'<div class="metric-card"><h2 style="margin:0;color:#FFFFFF!important;">{genres_count}</h2><p style="color:#808080;margin:0;">Categorical Genres</p></div>', unsafe_allow_html=True)

with kpi_col4:
    # Gauge Chart
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = len(filtered_df),
        domain = {'x': [0, 1], 'y': [0, 1]},
        delta = {'reference': TARGET_INVENTORY, 'position': "top"},
        title = {'text': "Inventory Ingestion Target KPI", 'font': {'size': 14, 'color': "white"}},
        gauge = {
            'axis': {'range': [None, TARGET_INVENTORY * 1.2], 'tickcolor': "white"},
            'bar': {'color': "#E50914"},
            'steps': [
                {'range': [0, TARGET_INVENTORY * 0.6], 'color': "#333333"},
                {'range': [TARGET_INVENTORY * 0.6, TARGET_INVENTORY], 'color': "#555555"}
            ],
            'threshold': {'line': {'color': "white", 'width': 4}, 'thickness': 0.75, 'value': TARGET_INVENTORY}
        }
    ))
    fig_gauge.update_layout(template="plotly_dark", height=160, paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=30, b=10))
    st.plotly_chart(fig_gauge, width="stretch")

st.markdown("---")

# ==========================================
# 5. MULTI-TAB MATRIX ARCHITECTURE
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Operational Trends & Ribbons", 
    "🍕 Part-to-Whole & Pipelines", 
    "🔬 Detail Relationships & Decomposition", 
    "🌍 Geographic Footprints"
])

# ------------------------------------------
# TAB 1: CORE TRENDS (BAR, COLUMN, LINE, COMBO, RIBBON)
# ------------------------------------------
with tab1:
    st.markdown("<h3 class='section-header'>Bar, Column, Line, Combo & Ribbon Charting Matrix</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Line & Combo Engine (Intake Pacing)")
        trend_data = filtered_df.groupby('year_added').size().reset_index(name='Volume')
        trend_data['Running Total'] = trend_data['Volume'].cumsum()
        
        # Combo Chart: Bars + Line Overlay
        fig_combo = go.Figure()
        fig_combo.add_trace(go.Bar(x=trend_data['year_added'], y=trend_data['Volume'], name="Yearly Additions", marker_color='#B30710'))
        fig_combo.add_trace(go.Scatter(x=trend_data['year_added'], y=trend_data['Running Total'], name="Total Scale Accumulation", yaxis="y2", line=dict(color='#E50914', width=3)))
        
        fig_combo.update_layout(
            template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            yaxis=dict(title="Yearly Volume Drops"),
            yaxis2=dict(title="Cumulative Database Scale", overlaying="y", side="right"),
            margin=dict(l=20, r=20, t=30, b=20)
        )
        st.plotly_chart(fig_combo, width="stretch")
        
    with col2:
        st.subheader("Premium Ribbon Chart (Territory Ranking Switches Over Time)")
        top_countries = list(df['country'].value_counts().head(4).index)
        ribbon_raw = filtered_df[filtered_df['country'].isin(top_countries)]
        ribbon_df = ribbon_raw.groupby(['year_added', 'country']).size().reset_index(name='Count')
        
        fig_ribbon = px.area(ribbon_df, x="year_added", y="Count", color="country", line_group="country",
                             color_discrete_sequence=['#E50914', '#B30710', '#7A050B', '#333333'])
        fig_ribbon.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_ribbon, width="stretch")

# ------------------------------------------
# TAB 2: PART-TO-WHOLE & PROCESS FLOWS (PIE, DONUT, TREEMAP, WATERFALL)
# ------------------------------------------
with tab2:
    st.markdown("<h3 class='section-header'>Hierarchies, Structural Partitions & Pipelines</h3>", unsafe_allow_html=True)
    
    col_t2_1, col_t2_2 = st.columns(2)
    
    with col_t2_1:
        st.subheader("Donut Model Share vs Treemap Hierarchies")
        pie_data = filtered_df['rating'].value_counts().head(5).reset_index()
        pie_data.columns = ['Rating', 'Count']
        fig_donut = px.pie(pie_data, names='Rating', values='Count', hole=0.5,
                           color_discrete_sequence=["#E509C0", '#B30710', '#7A050B', '#4A0003', '#221F1F'])
        fig_donut.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_donut, width="stretch")
        
        # Treemap Integration
        tree_raw = filtered_df.copy()
        tree_data = tree_raw.groupby(['country', 'rating']).size().reset_index(name='Volume')
        fig_tree = px.treemap(tree_data, path=['country', 'rating'], values='Volume',
                              color_discrete_sequence=['#B30710', '#7A050B'])
        fig_tree.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_tree, width="stretch")
        
    with col_t2_2:
        st.subheader("Waterfall Variance Pacing")
        # Waterfall Chart Simulation
        fig_waterfall = go.Figure(go.Waterfall(
            name = "Inventory Inflow/Outflow Delta", orientation = "v",
            measure = ["relative", "relative", "total", "relative", "relative", "total"],
            x = ["2022 Base Ingest", "2023 Expired Rights", "2023 End Balance", "2024 New Licensing", "2025 Originals Expansion", "2025 Target Balance"],
            text = ["+800", "-300", "500", "+600", "+400", "1500"],
            y = [800, -300, 0, 600, 400, 0],
            connector = {"line":{"color":"#E50914"}},
            decreasing = {"marker":{"color":"#7A050B"}},
            increasing = {"marker":{"color":"#E50914"}},
            totals = {"marker":{"color":"#FFFFFF"}}
        ))
        fig_waterfall.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_waterfall, width="stretch")

# ------------------------------------------
# TAB 3: RELATIONSHIPS, SCATTERS & DECOMPOSITION TREES
# ------------------------------------------
with tab3:
    st.markdown("<h3 class='section-header'>Relationships, Clustering & Multi-Dimensional Deep Dives</h3>", unsafe_allow_html=True)
    
    col_t3_1, col_t3_2 = st.columns([1.5, 1])
    
    with col_t3_1:
        st.subheader("Scatter & Bubble Coordinate Space")
        scatter_data = filtered_df.groupby(['release_year', 'year_added', 'rating']).size().reset_index(name='Density')
        fig_bubble = px.scatter(scatter_data, x="release_year", y="year_added", size="Density", color="rating",
                                hover_name="rating", size_max=40, color_discrete_sequence=px.colors.sequential.Reds)
        fig_bubble.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_bubble, width="stretch")
        
    with col_t3_2:
        st.subheader("AI-Engineered Functional Decomposition Tree")
        decomp_level_1 = st.selectbox("Root Dimension Breakdown Axis:", ["country", "rating"])
        decomp_vals = filtered_df[decomp_level_1].value_counts().head(4)
        
        for name, count in decomp_vals.items():
            st.markdown(f"**🌿 Level Node: {str(name).upper()}**")
            st.progress(min(float(count / len(filtered_df)), 1.0))
            st.caption(f"Asset density tracking weight: {count} listings inside current viewport array.")

    st.markdown("### Multi-Dimensional Master Matrix Ledger")
    matrix_df = filtered_df.pivot_table(index='country', columns='rating', values='year_added', aggfunc='count', fill_value=0)
    st.dataframe(matrix_df.style.background_gradient(cmap='Reds'), use_container_width=True)

# ------------------------------------------
# TAB 4: GEOGRAPHIC MAP MAPS SYSTEM
# ------------------------------------------
with tab4:
    st.markdown("<h3 class='section-header'>Global Geographic GIS Spatial Matrix</h3>", unsafe_allow_html=True)
    
    geo_df = filtered_df.groupby('country').size().reset_index(name='Asset Density')
    
    map_type = st.radio("Switch Map Projection Geometry Layer:", ["Filled Density Map (Choropleth)", "Basic Spatial Bubble Map"], horizontal=True)
    
    if "Filled" in map_type:
        fig_map = px.choropleth(geo_df, locations="country", locationmode="country names",
                                color="Asset Density", color_continuous_scale=px.colors.sequential.Reds)
    else:
        fig_map = px.scatter_geo(geo_df, locations="country", locationmode="country names",
                                 size="Asset Density", color="Asset Density", color_continuous_scale=px.colors.sequential.Reds)
        
    fig_map.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', geo=dict(bgcolor='rgba(0,0,0,0)', showframe=False))
    st.plotly_chart(fig_map, width="stretch")
