import streamlit as st
import pandas as pd 
import preprocess,helper
df = preprocess.preporcess()
user_menu = st.sidebar.radio( " select an options",
                ("Medal Tally", "overall-Analysis",'Country_wise- Analysis', 'Athlete_wise Analysis')
                )
st.dataframe(df)

if user_menu == "Medal Tally":
    medall = helper.medaltally (df)
    st.dataframe(medall)