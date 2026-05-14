from collections import Counter

EMOTION_KEYWORDS = {
    "fear": ["怕", "风险", "后悔", "损失"],
    "shock": ["震惊", "不敢相信", "居然", "天啊"],
    "trust": ["真实", "亲测", "认证", "医生"],
    "urgency": ["马上", "限时", "今天", "最后"]
}


def detect_emotion_profile(text: str) -> dict:
    text = text or ""
    score = Counter()
    for emotion, keywords in EMOTION_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                score[emotion] += 1
    total = sum(score.values()) or 1
    return {k: round(v / total, 3) for k, v in score.items()}
