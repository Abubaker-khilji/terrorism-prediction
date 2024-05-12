import pickle 
from pathlib import  Path

import streamlit_authenticator as stauth

import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static
import folium
from folium.plugins import FastMarkerCluster, Fullscreen
from datetime import datetime
from plotly import graph_objs as go
from generate_key import sign_up, fetch_users



st.set_page_config(
        page_title="Tech against terroism",
        page_icon="logo.png",
        layout="wide",
)

#user authentication

try:
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []

    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)

    email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

    info, info1 = st.columns(2)

    if not authentication_status:
        sign_up()

    if username:
        if username in usernames:
            if authentication_status:
              

                padding = 0
                uthenticator.logout("Logout","sidebar")
                st.sidebar.title(f"welcome{username}")
                col1, col2 = st.sidebar.columns([40,60])
                col1.image("logo.png",width=100)
                st.image("dataset-cover.png", use_column_width=True)
                col2.title("TERROISM")
                col2.text("still developing")
                col3, col4 = st.sidebar.columns(2)



                data = pd.read_csv("global-terrorism.csv")
                data.replace(r'\s+', np.nan, regex=True)
                data['DATE'] = pd.to_datetime(data['DATE']).dt.date
                data['DEAD'] = data['DEAD'].astype('Int64')
                data['INJURED'] = data['INJURED'].astype('Int64')



                fromdate = col3.date_input(
                    "FROM", value=(pd.Timestamp("2001-01-01").date()), min_value=(pd.Timestamp(min(data['DATE'])).date()), max_value=(pd.Timestamp(max(data['DATE'])).date()))
                todate = col4.date_input(
                    "TO", value=(pd.Timestamp(max(data['DATE'])).date()), min_value=(pd.Timestamp(min(data['DATE'])).date()), max_value=(pd.Timestamp(max(data['DATE'])).date()))


                countries = list(data["COUNTRY"].sort_values().unique())
                countries = [x for x in countries if pd.isnull(x) == False]
                countries.insert(0, "*")
                country = st.sidebar.multiselect("COUNTRY", countries, default="*")


                regions = list(data["REGION"].sort_values().unique())
                regions = [x for x in regions if pd.isnull(x) == False]
                regions.insert(0, "*")
                region = st.sidebar.multiselect("REGION", regions, default="*")



                mask = (data['DATE'] > np.datetime64(fromdate)) & (
                    data['DATE'] <= np.datetime64(todate))
                data = data.loc[mask]

                if "*" not in country:
                    mask = data["COUNTRY"].isin(country)
                    data = data[mask]

                if "*" not in region:
                    mask = data["REGION"].isin(region)
                    data = data[mask]


                lat = []
                lon = []
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

                folium_map = folium.Map(tiles='cartodbpositron')
                FastMarkerCluster(data=list(zip(lat, lon)),
                                callback=callback).add_to(folium_map)
                Fullscreen().add_to(folium_map)
                folium_static(folium_map, width=800)
                col4, col3 = st.columns([20,80])


                st.subheader("DEAD")
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=data['DATE'], y=data['DEAD'].groupby(data['DATE']).sum()))
                st.plotly_chart(fig, use_container_width=True, config = {'displayModeBar': False})

                st.subheader("INJURED")
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=data['DATE'], y=data['INJURED'].groupby(data['DATE']).sum()))
                st.plotly_chart(fig, use_container_width=True, config = {'displayModeBar': False})

                st.sidebar.title("Statistics")
                st.sidebar.text("Attacks: "+str(len(data)) +
                                "\nCountries: "+str(len(data["COUNTRY"].unique()))+"\nDeaths: "+str(int(data["DEAD"].sum())))
                if st.sidebar.button("RERUN"):
                    st.experimental_rerun()
                st.dataframe(data)

                @st.cache_data
                def convert_df(df):
                   return df.to_csv().encode('utf-8')

                csv = convert_df(data)

                st.download_button(
                  "DOWNLOAD",
                   csv,
                   "global-terrorism-copy.csv",
                   "text/csv",
                   key='download-csv'
                )
            else:
                 with info:
                    st.warning('Please feed in your credentials')
        else:
          with info:
            st.warning('Username does not exist, Please Sign up')

    elif not authentication_status:
                             with info:
                                st.error('Incorrect Password or username')

except Exception as e:
    st.error(f'An error occurred: {e}')