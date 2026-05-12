import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="BrickView AI",
    page_icon="🏠",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
df = pd.read_json("listings_final_expanded.json")

# lowercase columns
df.columns = df.columns.str.lower()

# ---------------- STYLING ----------------
st.markdown("""
<style>

body {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #141e30);
}

h1 {
    color: cyan;
    text-align: center;
}

.stMetric {
    background: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🏠 BrickView AI Dashboard")

st.markdown("### Real Estate Analytics Platform")

# ---------------- SEARCH ----------------
search = st.text_input("🔍 Search City")

if search:
    df = df[df["city"].str.contains(search, case=False)]

# ---------------- KPI ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Properties", len(df))

with col2:
    st.metric("Average Price", f"₹ {round(df['price'].mean(),2)}")

with col3:
    st.metric("Highest Price", f"₹ {df['price'].max()}")

# ---------------- DATAFRAME ----------------
st.subheader("📋 Property Listings")

st.dataframe(df)

# ---------------- CHARTS ----------------
col4, col5 = st.columns(2)

with col4:

    city_counts = df["city"].value_counts().reset_index()

    city_counts.columns = ["city", "count"]

    fig_bar = px.bar(
        city_counts,
        x="city",
        y="count",
        title="Properties by City"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

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

    st.plotly_chart(fig_donut, use_container_width=True)

# ---------------- LINE CHART ----------------
avg_price = df.groupby("city")["price"].mean().reset_index()

fig_line = px.line(
    avg_price,
    x="city",
    y="price",
    markers=True,
    title="Average Price by City"
)

st.plotly_chart(fig_line, use_container_width=True)

# ---------------- MAP ----------------
if "latitude" in df.columns and "longitude" in df.columns:

    st.subheader("🗺️ Property Locations")

    st.map(df[["latitude", "longitude"]])

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown("### 🚀 Built with Python, Plotly & Streamlit")
