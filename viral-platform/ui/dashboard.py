import pandas as pd
import streamlit as st

from database.sqlite import top_hooks


def render_dashboard() -> None:
    st.header("📊 数据总览")
    col1, col2, col3 = st.columns(3)
    col1.metric("分析视频", "128")
    col2.metric("爆款Hook", "36")
    col3.metric("平均CTR", "4.7%")

    st.subheader("🔥 爆款 Hook 排行")
    hooks = top_hooks(limit=10)
    if hooks:
        st.dataframe(pd.DataFrame(hooks), use_container_width=True)
    else:
        st.info("暂无数据，请先分析视频并入库。")
