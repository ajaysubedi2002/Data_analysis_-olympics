import streamlit as st
import pandas as pd 

st.sidebar.radio( " select an options",
                ("Medal Tally", "overall Analysis",'Countrywuse Analysis', 'Athletewise Analysis')
                )