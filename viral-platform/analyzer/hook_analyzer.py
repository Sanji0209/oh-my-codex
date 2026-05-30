from ai.openai_client import client, get_model_name
from ai.prompts import HOOK_ANALYZER_SYSTEM_PROMPT, build_hook_analysis_prompt


def analyze_hook(script: str, market: str = "BR") -> str:
    response = client.chat.completions.create(
        model=get_model_name(),
        messages=[
            {"role": "system", "content": HOOK_ANALYZER_SYSTEM_PROMPT},
            {"role": "user", "content": build_hook_analysis_prompt(script, market=market)},
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content or ""
