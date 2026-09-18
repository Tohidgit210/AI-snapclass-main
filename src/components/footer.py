
import streamlit as st





def footer_home():
    st.markdown(
        '<div style="display:flex; justify-content:center; '
        'align-items:center; gap:8px; margin-top:2rem;">'
        '<span style="color:white; font-weight:600;">'
        'Created with ❤️ by</span>'
        '<span style="color:#67e8f9; font-size:19px; '
        'font-weight:800;">SnapAttend</span>'
        '</div>',
        unsafe_allow_html=True
    )

def footer_dashboard():
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px;
                    justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:black;">
                Created with ❤️ by
            </p>
            <span style="color:#06b6d4; font-size:19px;
                         font-weight:800;">
                SnapAttend
            </span>
        </div>
    """, unsafe_allow_html=True)