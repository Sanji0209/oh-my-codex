from pathlib import Path
import streamlit as st

from analyzer.hook_analyzer import analyze_hook


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def render_upload_page() -> None:
    st.header("🎬 视频分析")
    uploaded_file = st.file_uploader("上传 TikTok 视频", type=["mp4"])

    if uploaded_file is None:
        return

    save_path = UPLOAD_DIR / uploaded_file.name
    save_path.write_bytes(uploaded_file.getbuffer())
    st.success(f"上传成功：{save_path.name}")

    script = st.text_area("可选：粘贴已转写脚本（若为空则后续可接入自动转写）", height=180)
    market = st.selectbox("市场", ["BR", "US", "MX"], index=0)

    if st.button("开始 AI 拆解", type="primary"):
        if not script.strip():
            st.warning("当前版本请先粘贴脚本文本，下一步可接入自动转写流程。")
            return
        with st.spinner("AI 正在分析..."):
            result = analyze_hook(script, market)
        st.subheader("🧠 AI 拆解结果")
        st.markdown(result)
