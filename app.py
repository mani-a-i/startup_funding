import streamlit as st
import pandas as pd
import data_analysis as dn

df= pd.read_csv('Cleaned_startup.csv')

st.sidebar.title('Startup funding analysis')
option = st.sidebar.selectbox('Select from below',['Overall Analysis','Startup','Investor'])

def show_startup(startup):
    st.title(startup)
    st.subheader(dn.startup_info(startup))

def show_investor(investor):
    st.title(investor)
    st.subheader('Most Recent Investments')
    st.dataframe(dn.investor_recent(investor))

if option == 'Overall Analysis':
    st.title('Overall Analysis')    

elif option == 'Startup':
    startup = st.sidebar.selectbox('Startups:',dn.startup_names())
    btn = st.sidebar.button(f'find details')
    
    if btn:
        show_startup(startup)


else:
    investor = st.sidebar.selectbox('Investors', dn.investor_names())
    btn = st.sidebar.button(f'find details')
    if btn:
        show_investor(investor)