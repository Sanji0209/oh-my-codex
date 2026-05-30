from faster_whisper import WhisperModel

_model = WhisperModel("small", device="cpu", compute_type="int8")


def transcribe(audio_path: str) -> str:
    segments, _ = _model.transcribe(audio_path)
    return "\n".join(segment.text.strip() for segment in segments if segment.text.strip())
