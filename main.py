import os

WORD = "leash"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = WORD
    if not (1 <= len(text) <= 20):
        raise SystemExit("entry must be 1 to 20 characters")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if len(text.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back verification failed")


if __name__ == "__main__":
    main()
