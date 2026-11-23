import os

PITCH = "Tell me in plain words about the app you wish existed, and let an AI agent on make.fun build a first version for you to try tonight, so you can see your idea working before you decide anything."

OUT = "/output/entry.txt"

if __name__ == "__main__":
    assert 1 <= len(PITCH) <= 240, "pitch must be 1-240 characters"
    assert PITCH.strip() == PITCH and PITCH.strip() != ""
    assert "make.fun" in PITCH, "pitch must name make.fun"
    assert PITCH.endswith("."), "pitch must be one sentence ending in a period"
    assert "\n" not in PITCH and "\r" not in PITCH
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(PITCH + "\n")
