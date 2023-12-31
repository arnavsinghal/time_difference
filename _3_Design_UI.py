import streamlit as st
from datetime import datetime

# Define the two times as strings
 

# Specify the time format
time_format = "%H:%M:%S"

time1_str = st.text_input("please put later time here like 17:34:06")
time2_str = st.text_input("please put earlier time here like 12:50:05")

time1_str = time1_str.replace(".",":")
time2_str = time1_str.replace(".",":")

time1_str = time1_str.replace("-",":")
time2_str = time1_str.replace("-",":")

submit = st.button("Compute Difference")
if submit:
    # Convert the string times to datetime objects
    time1 = datetime.strptime(time1_str, time_format)
    time2 = datetime.strptime(time2_str, time_format)

    # Calculate the time difference
    time_difference = time1 - time2

    # Print the result
    st.write("Time difference:", time_difference)
