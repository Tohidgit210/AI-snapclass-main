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
    st.markdown(
        """
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
            margin-top: 2rem;
            padding: 12px;
            border-top: 1px solid #e5e7eb;
            font-family: Arial, sans-serif;
        ">
            <span style="
                font-size: 13px;
                color: #64748b;
            ">
                Powered by
            </span>

            <span style="
                font-size: 16px;
                font-weight: 800;
                letter-spacing: 0.5px;
                background: linear-gradient(
                    90deg, #06b6d4, #6366f1
                );
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            ">
                SnapAttend
            </span>

            <span style="font-size: 16px;">
                ✦
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )