CTA_KEYWORDS = ["立即", "马上", "点击", "下单", "抢购", "私信", "领取"]


def extract_cta(text: str) -> list[str]:
    lines = [line.strip() for line in (text or "").splitlines() if line.strip()]
    return [line for line in lines if any(k in line for k in CTA_KEYWORDS)]
