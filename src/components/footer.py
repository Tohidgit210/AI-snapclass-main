


import streamlit as st

def footer_home():
    logo_url = "https://tse1.mm.bing.net/th/id/OIP.eOED9H2dmVT3FMdInMGpSQHaHa?r=0&pid=Api&h=220&P=0"

    st.markdown(f"""
        <div style="
            margin-top: 2rem;
            display: flex;
            gap: 8px;
            justify-content: center;
            align-items: center;
        ">
            <p style="
                font-weight: bold;
                color: white;
                margin: 0;
            ">
                Created with ❤️ by SnapClass
            </p>

            <img src="{logo_url}"
                 style="height: 25px; width: 25px;
                        object-fit: contain;" />
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://tse1.mm.bing.net/th/id/OIP.eOED9H2dmVT3FMdInMGpSQHaHa?r=0&pid=Api&h=220&P=0"

    st.markdown(f"""
        <div style="
            margin-top: 2rem;
            display: flex;
            gap: 8px;
            justify-content: center;
            align-items: center;
        ">
            <p style="
                font-weight: bold;
                color: black;
                margin: 0;
            ">
                Created with ❤️ by SnapClass
            </p>

            <img src="{logo_url}"
                 style="height: 25px; width: 25px;
                        object-fit: contain;" />
        </div>
    """, unsafe_allow_html=True)