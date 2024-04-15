import streamlit as st
from datetime import datetime, timedelta

from utils import (
    get_file_from_s3,
    filter_df_on_dates,
)

# Get data #
shark_sightings = get_file_from_s3(
    bucket_name="mada-whales-python", object_key="sharks/sightings.parquet"
)

megaf_sightings = get_file_from_s3(
    bucket_name="mada-whales-python", object_key="megaf/sightings.parquet"
)


st.title("About Page")
st.write(
    """This is the About Page.
    Here you can share information about your app or project."""
)

one_year_ago = datetime.now() - timedelta(days=365)
start_date = st.date_input("Start date", value=one_year_ago)
end_date = st.date_input("End date", value="today", min_value=start_date)

raw_select = st.selectbox("Select a dataset", ["Sharks", "Megafauna"])
if raw_select == "Sharks":
    st.dataframe(filter_df_on_dates(shark_sightings, start_date, end_date))
elif raw_select == "Megafauna":
    st.dataframe(filter_df_on_dates(megaf_sightings, start_date, end_date))
