from ai.openai_client import client, get_model_name


def generate_variants(product: str, country: str, pain_point: str) -> str:
    prompt = f"""
请基于以下信息生成 TikTok 广告脚本方案：
- 产品：{product}
- 国家：{country}
- 核心痛点：{pain_point}

输出：
1) 10 个 Hook
2) 5 个 CTA
3) 男性版本脚本
4) 女性版本脚本
5) 本地化版本脚本
"""
    response = client.chat.completions.create(
        model=get_model_name(),
        messages=[
            {"role": "system", "content": "你是电商广告创意总监"},
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
    )
    return response.choices[0].message.content or ""
