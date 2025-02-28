import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_folium import folium_static
import folium
from folium.plugins import FastMarkerCluster, Fullscreen
from datetime import datetime
from plotly import graph_objs as go

# Load the LightGBM model
with open("best_lightgbm_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

st.set_page_config(
        page_title="terrorism prediction",
        page_icon="logo.JPEG",
        layout="wide",
)

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

# Sidebar Content
col1, col2 = st.sidebar.columns([40,60])
col1.image("logo.JPEG",width=100)
st.image("dataset-cover.JPEG", use_container_width=True)
col2.title("Fyp Terrorism Project")
col2.text("v0.0.2")
col3, col4 = st.sidebar.columns(2)

# Load the data
data = pd.read_csv("global-terrorism.csv")
data.replace(r'\s+', np.nan, regex=True)
data['DATE'] = pd.to_datetime(data['DATE']).dt.date
data['DEAD'] = data['DEAD'].astype('Int64')
data['INJURED'] = data['INJURED'].astype('Int64')

# Date Inputs for Filtering Data
fromdate = col3.date_input(
    "FROM", value=(pd.Timestamp("2001-01-01").date()), min_value=(pd.Timestamp(min(data['DATE'])).date()), max_value=(pd.Timestamp(max(data['DATE'])).date()))
todate = col4.date_input(
    "TO", value=(pd.Timestamp(max(data['DATE'])).date()), min_value=(pd.Timestamp(min(data['DATE'])).date()), max_value=(pd.Timestamp(max(data['DATE'])).date()))

# Additional Filters for Country, Region, Perpetrator, and Category
countries = list(data["COUNTRY"].sort_values().unique())
countries = [x for x in countries if pd.isnull(x) == False]
countries.insert(0, "*")
country = st.sidebar.multiselect("COUNTRY", countries, default="*")
regions = list(data["REGION"].sort_values().unique())
regions = [x for x in regions if pd.isnull(x) == False]
regions.insert(0, "*")
region = st.sidebar.multiselect("REGION", regions, default="*")
perpetrators = list(data["PERPETRATOR"].sort_values().unique())
perpetrators = [x for x in perpetrators if pd.isnull(x) == False]
perpetrators.insert(0, "*")
perpetrator = st.sidebar.multiselect("PERPETRATOR", perpetrators, default="*")
categories = list(data["CATEGORY"].sort_values().unique())
categories = [x for x in categories if pd.isnull(x) == False]
categories.insert(0, "*")
category = st.sidebar.multiselect("CATEGORY", categories, default="*")

# Data Filtering Based on User Inputs
mask = (data['DATE'] > np.datetime64(fromdate)) & (data['DATE'] <= np.datetime64(todate))
data = data.loc[mask]
if "*" not in country:
    mask = data["COUNTRY"].isin(country)
    data = data[mask]
if "*" not in region:
    mask = data["REGION"].isin(region)
    data = data[mask]
if "*" not in perpetrator:
    mask = data["PERPETRATOR"].isin(perpetrator)
    data = data[mask]
if "*" not in category:
    mask = data["CATEGORY"].isin(category)
    data = data[mask]

# Map Generation for Visualization
lat, lon = [], []
for coord in list(data['COORDINATES'].values):
    try:
        lat.append(coord.split(",")[0])
        lon.append(coord.split(",")[1])
    except:
        continue

callback = """\
function (row) {
    var marker;
    marker = L.circle(new L.LatLng(row[0], row[1]), {color:'red'});
    return marker;
};
"""
make_map_responsive= """
 <style>
 [title~="st.iframe"] { width: 100%}
 </style>
"""
st.markdown(make_map_responsive, unsafe_allow_html=True)

# Display Map
folium_map = folium.Map(tiles='cartodbpositron')
FastMarkerCluster(data=list(zip(lat, lon)), callback=callback).add_to(folium_map)
Fullscreen().add_to(folium_map)
folium_static(folium_map, width=800)

# Frequency and Distribution Selection
col4, col3 = st.columns([20,80])
freq = col4.radio("Frequency",('DEAD', 'INJURED'))
dist = col4.radio("Distribution",('CATEGORY', 'PERPETRATOR', 'REGION', 'SUBREGION', 'COUNTRY', 'STATE', 'CITY'))

# Plot Pie Chart
fig = go.Figure(data=[go.Pie(labels=list(data[freq].groupby(data[dist]).sum().sort_values().nlargest(5).index),
                            values=list(data[freq].groupby(data[dist]).sum().sort_values().nlargest(5)))]
                                )

fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20, marker=dict(line=dict(color='#000000', width=2)))
col3.plotly_chart(fig, use_container_width=True, config = {'displayModeBar': False})

# Plot Dead and Injured
st.subheader("DEAD")
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['DATE'], y=data['DEAD'].groupby(data['DATE']).sum()))
st.plotly_chart(fig, use_container_width=True, config = {'displayModeBar': False})

st.subheader("INJURED")
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['DATE'], y=data['INJURED'].groupby(data['DATE']).sum()))
st.plotly_chart(fig, use_container_width=True, config = {'displayModeBar': False})

# Prediction Section
st.subheader("Prediction")
input_features = {
    'feature1': st.number_input("Feature 1", min_value=0.0, step=0.1),
    'feature2': st.number_input("Feature 2", min_value=0.0, step=0.1),
    # Add more inputs as needed
}

# Predict Button
if st.button("Predict"):
    features = np.array([[input_features['feature1'], input_features['feature2']]])
    prediction = model.predict(features)
    st.success(f"Prediction: {'Positive' if prediction[0] == 1 else 'Negative'}")

# Sidebar Statistics and Download Option
st.sidebar.title("Statistics")
st.sidebar.text(f"Attacks: {len(data)}\nRegions: {len(data['REGION'].unique())}\nCountries: {len(data['COUNTRY'].unique())}\nPerpetrators: {len(data['PERPETRATOR'].unique())}\nDeaths: {int(data['DEAD'].sum())}\nInjuries: {int(data['INJURED'].sum())}")
if st.sidebar.button("RERUN"):
    st.experimental_rerun()

# Dataframe Display
st.dataframe(data)

# CSV Download Button
@st.cache_data
def convert_df(df):
   return df.to_csv().encode('utf-8')

csv = convert_df(data)
st.download_button("DOWNLOAD", csv, "global-terrorism.csv", "text/csv", key='download-csv')
