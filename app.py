import streamlit as st
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="BrickView AI",
    page_icon="🏠",
    layout="wide"
)

# ---------------- FUTURISTIC UI ----------------
import pandas as pd

df = pd.read_json("listings_final_expanded.json")

df.columns = df.columns.str.lower()
<style>

/* Animated Gradient Background */
body {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #141e30);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Main */
.main {
    color: white;
}

/* Title */
h1 {
    text-align: center;
    color: cyan;
    font-size: 60px;
    text-shadow: 0px 0px 25px cyan;
}

/* Headers */
h2, h3 {
    color: #00ffd5;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
}

/* KPI Cards */
.stMetric {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 15px;
    box-shadow: 0px 0px 25px rgba(0,255,255,0.2);
    transition: 0.3s;
}

.stMetric:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 35px cyan;
}

/* Buttons */
.stButton button,
.stDownloadButton button {
    background: linear-gradient(to right, cyan, #00bfff);
    color: black;
    border-radius: 12px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton button:hover,
.stDownloadButton button:hover {
    transform: scale(1.08);
    box-shadow: 0px 0px 25px cyan;
}

/* Tables */
.stDataFrame {
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0px 0px 20px rgba(0,255,255,0.2);
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATABASE CONNECTION ----------------

# lowercase columns
df.columns = df.columns.str.lower()

# ---------------- TITLE ----------------
st.title("🏠 BrickView AI Dashboard")

st.markdown("### Futuristic Real Estate Intelligence Platform")

# ---------------- EXECUTIVE DASHBOARD ----------------

st.header("🚀 Executive Dashboard")

total_properties = len(df)

avg_price = round(df["price"].mean(), 2)

highest_price = df["price"].max()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🏠 Total Properties", total_properties)

with col2:
    st.metric("💰 Avg Price", f"₹ {avg_price}")

with col3:
    st.metric("🚀 Highest Price", f"₹ {highest_price}")

# ---------------- SMART EXPLORER ----------------

st.header("🔍 Smart Property Explorer")

search_city = st.text_input("🔎 Search City")

if search_city:
    df = df[df["city"].str.contains(search_city, case=False)]

selected_city = st.selectbox(
    "📍 Select City",
    df["city"].unique()
)

filtered_df = df[df["city"] == selected_city]

# Price Slider
min_price = int(filtered_df["price"].min())
max_price = int(filtered_df["price"].max())

price_range = st.slider(
    "💰 Select Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

filtered_df = filtered_df[
    (filtered_df["price"] >= price_range[0]) &
    (filtered_df["price"] <= price_range[1])
]

st.dataframe(filtered_df)

# Download Button
csv = filtered_df.to_csv(index=False)

st.download_button(
    "⬇ Download Property Data",
    csv,
    "properties.csv",
    "text/csv"
)

# ---------------- AI VISUAL ANALYTICS ----------------

st.header("📊 AI Visual Analytics")

col4, col5 = st.columns(2)

# -------- LINE CHART --------
with col4:

    avg_price_city = df.groupby("city")["price"].mean().reset_index()

    fig_line = px.line(
        avg_price_city,
        x="city",
        y="price",
        title="Average Price by City",
        markers=True
    )

    fig_line.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )

    st.plotly_chart(fig_line, use_container_width=True)

# -------- DONUT CHART --------
with col5:

    property_counts = df["property_type"].value_counts().reset_index()

    property_counts.columns = ["property_type", "count"]

    fig_donut = px.pie(
        property_counts,
        names="property_type",
        values="count",
        hole=0.5,
        title="Property Type Distribution"
    )

    fig_donut.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white'
    )

    st.plotly_chart(fig_donut, use_container_width=True)

# ---------------- BAR CHART ----------------

city_counts = df["city"].value_counts().reset_index()

city_counts.columns = ["city", "count"]

fig_bar = px.bar(
    city_counts,
    x="city",
    y="count",
    title="Properties by City",
    color="count"
)

fig_bar.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)

st.plotly_chart(fig_bar, use_container_width=True)

# ---------------- HISTOGRAM ----------------

fig_hist = px.histogram(
    df,
    x="price",
    nbins=20,
    title="Price Distribution",
    color_discrete_sequence=["cyan"]
)

fig_hist.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='white'
)

st.plotly_chart(fig_hist, use_container_width=True)

# ---------------- MARKET INSIGHTS ----------------

st.header("📈 Market Intelligence")

highest_city = df.groupby("city")["price"].mean().idxmax()

lowest_city = df.groupby("city")["price"].mean().idxmin()

col6, col7 = st.columns(2)

with col6:
    st.success(f"🏆 Highest Avg Price City: {highest_city}")

with col7:
    st.info(f"💡 Lowest Avg Price City: {lowest_city}")

st.subheader("🏘️ Top Property Cities")

top_cities = df["city"].value_counts()

st.bar_chart(top_cities)

# ---------------- PROPERTY MAP ----------------

st.header("🗺️ Property Locations")

if 'latitude' in df.columns and 'longitude' in df.columns:
    st.map(df[["latitude", "longitude"]])



# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("### 🚀 Built with Python, SQL, Plotly & Streamlit")




