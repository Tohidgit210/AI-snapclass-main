
import streamlit as st





def footer_home():
    logo_url = "https://tse1.mm.bing.net/th/id/OIP.eOED9H2dmVT3FMdInMGpSQHaHa?r=0&pid=Api&h=220&P=0"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by snapclass </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://tse1.mm.bing.net/th/id/OIP.eOED9H2dmVT3FMdInMGpSQHaHa?r=0&pid=Api&h=220&P=0"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by snapclass </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)