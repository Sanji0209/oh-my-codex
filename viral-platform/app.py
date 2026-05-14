import streamlit as st
from dotenv import load_dotenv

from database.sqlite import init_db
from ui.analytics_page import render_roi_page
from ui.dashboard import render_dashboard
from ui.upload_page import render_upload_page

load_dotenv()
init_db()

st.set_page_config(page_title="TikTok Viral Analyzer", page_icon="🔥", layout="wide")
st.title("🔥 TikTok Viral Analyzer")

st.sidebar.title("功能菜单")
menu = st.sidebar.radio(
    "选择功能",
    ["Dashboard", "视频分析", "Hook数据库", "ROI分析", "AI仿爆款", "设置"],
)

if menu == "Dashboard":
    render_dashboard()
elif menu == "视频分析":
    render_upload_page()
elif menu == "Hook数据库":
    st.header("🔥 Hook 数据库")
    st.caption("可在后续版本加入标签筛选、语义检索、相似 Hook 推荐。")
elif menu == "ROI分析":
    render_roi_page()
elif menu == "AI仿爆款":
    st.header("🧠 AI仿爆款")
    st.caption("可扩展产品输入后自动生成 Hook、CTA 与镜头脚本。")
else:
    st.header("⚙ 设置")
    st.caption("建议在 .env 中配置 OPENAI_API_KEY / MODEL_NAME / OPENAI_BASE_URL。")
