import cv2


def extract_frames(video_path: str, out_dir: str, every_n_frames: int = 30) -> list[str]:
    cap = cv2.VideoCapture(video_path)
    index = 0
    saved = 0
    paths: list[str] = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if index % every_n_frames == 0:
            path = f"{out_dir}/frame_{saved:05d}.jpg"
            cv2.imwrite(path, frame)
            paths.append(path)
            saved += 1
        index += 1

    cap.release()
    return paths
