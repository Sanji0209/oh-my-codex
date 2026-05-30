HOOK_ANALYZER_SYSTEM_PROMPT = "你是专业 TikTok 爆款分析师，输出要结构化、可执行、可落地。"


def build_hook_analysis_prompt(script: str, market: str = "BR") -> str:
    return f"""
请分析这个 TikTok 视频脚本并输出：
1) Hook 类型（可多选）
2) 前3秒逻辑（强开头/推进速度/痛点/视觉冲突）
3) 情绪结构（按时间轴）
4) 是否适合 {market} TikTok 市场（原因）
5) 为什么容易爆（CTR/Retention/转化角度）
6) 10个仿爆款 Hook
7) 5个强转化 CTA

脚本：
{script}
""".strip()
