import streamlit as st
from analyzer.roi_predictor import predict_roi_bucket


def render_roi_page() -> None:
    st.header("📈 ROI 分析")
    ctr = st.number_input("CTR (%)", min_value=0.0, value=4.7, step=0.1)
    retention = st.number_input("Retention (%)", min_value=0.0, value=38.0, step=0.5)
    cvr = st.number_input("CVR (%)", min_value=0.0, value=2.0, step=0.1)

    bucket = predict_roi_bucket(ctr=ctr, retention=retention / 10, cvr=cvr)
    st.metric("预测 ROI 档位", bucket)
