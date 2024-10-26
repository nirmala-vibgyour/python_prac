import requests
from selectorlib import Extractor
import mysql.connector
import streamlit as st
import plotly_express as px

#def writeData(data):
    
    # cursor.execute("ALTER TABLE weather MODIFY air_temp_min FLOAT(3,1)")
    # dataConnection.commit()
    # cursor.execute("ALTER TABLE weather MODIFY air_temp_avg FLOAT(3,1)")
    # dataConnection.commit()
    # cursor.execute("ALTER TABLE weather MODIFY air_temp_max FLOAT(3,1)")
    # dataConnection.commit()
    # cursor.execute("ALTER TABLE weather MODIFY air_temp_depar_normal DECIMAL(2,1)")


    # for i in range(len(data)):
    #     cursor.execute("UPDATE weather SET air_temp_depar_normal = %s WHERE date = %s", (data[i]['air_temperature_departure_from_normal'], data[i]['date']))

    #     print(data[i])
    #     cursor.execute("INSERT INTO weather (date, air_temp_min, air_temp_avg, air_temp_max, air_temp_depar_normal, precipitation) \
    #         VALUES (%s, %s, %s, %s, %s, %s)", (data[i]['date'], data[i]['air_temperature_minimum'], data[i]['air_temperature_average'], data[i]['air_temperature_maximum'], \
    #                 data[i]['air_temperature_departure_from_normal'], data[i]['precipitation']))
    #     dataConnection.commit()

#dataConnection.commit()

# cursor.close()
# dataConnection.close()

def sourceHtml(url):
    response = requests.get(url)
    return response.text

def extract_data(url):
    source = sourceHtml(url)
    extractor = Extractor.from_yaml_file("selectors.yaml")
    data = extractor.extract(source) # 'data' is a dict.
    climate_data = data['climate_data']
    climate_data.pop(0)
    climate_data.pop(0)
    return climate_data  # This will be a list of dictionaries.



if __name__ == "__main__":
    # url = "https://www.weatherandclimate.info/monitor/?id=42807&month=9&year=2024" 
    # climate_data = extract_data(url)
    # writeData(climate_data)
    dataConnection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'ex@mvibgyor2025',
        database = 'climate'
    )
    cursor = dataConnection.cursor()
    options = ['','Minimum Air Temperature', 'Average Air Temperature', 'Maximum Air Temperature', 'Departure From Normal Temperature', 'Precipitation']
    st.title("Climate in September")
    selected_option = st.selectbox("Select:", options)
    cursor.execute("SELECT {select} FROM weather")
    rows = cursor.fetchall()
    fig = px.line(rows, x=selected_option, y='Date', title=f"Changes in {selected_option} in the month of September, 2024")
    st.plotly_chart(fig)
    