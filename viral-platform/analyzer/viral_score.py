def compute_viral_score(has_strong_hook: bool, cta_count: int, emotion_density: float) -> float:
    score = 50.0
    if has_strong_hook:
        score += 20
    score += min(cta_count * 4, 20)
    score += min(emotion_density * 25, 10)
    return round(min(score, 100), 2)
