from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="en")


def run_ocr(image_path: str) -> str:
    result = ocr.ocr(image_path, cls=True)
    texts = []
    for line in result:
        for item in line:
            texts.append(item[1][0])
    return "\n".join(texts)
