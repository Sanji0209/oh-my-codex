from moviepy import VideoFileClip


def extract_audio(video_path: str, output_audio_path: str) -> str:
    with VideoFileClip(video_path) as clip:
        clip.audio.write_audiofile(output_audio_path, logger=None)
    return output_audio_path
