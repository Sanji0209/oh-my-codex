from pathlib import Path
from sqlalchemy import create_engine, text

DB_PATH = Path(__file__).resolve().parent / "hook_library.db"
engine = create_engine(f"sqlite:///{DB_PATH}", future=True)


def init_db() -> None:
    with engine.begin() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS hook_library (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hook_text TEXT NOT NULL,
            hook_type TEXT,
            ctr REAL DEFAULT 0,
            roi_bucket TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """))


def insert_hook(hook_text: str, hook_type: str, ctr: float, roi_bucket: str) -> None:
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO hook_library (hook_text, hook_type, ctr, roi_bucket) VALUES (:h, :t, :c, :r)"),
            {"h": hook_text, "t": hook_type, "c": ctr, "r": roi_bucket},
        )


def top_hooks(limit: int = 20) -> list[dict]:
    with engine.begin() as conn:
        rows = conn.execute(
            text("SELECT hook_text, hook_type, ctr, roi_bucket, created_at FROM hook_library ORDER BY ctr DESC LIMIT :limit"),
            {"limit": limit},
        ).mappings().all()
    return [dict(r) for r in rows]
