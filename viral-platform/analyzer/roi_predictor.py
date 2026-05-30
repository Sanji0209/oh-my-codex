def predict_roi_bucket(ctr: float, retention: float, cvr: float) -> str:
    weighted = ctr * 0.45 + retention * 0.35 + cvr * 0.2
    if weighted >= 6.0:
        return "高"
    if weighted >= 3.5:
        return "中"
    return "低"
