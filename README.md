# Pie-time πππ

Time and year displayed in **π units**. Because why not?

- **π time**: `decimal_hours / π` — a full 24h day ≈ `7.64π`
- **π year**: `year / π`

Live background + live metrics at 10 Hz, no blocking loops.

## Demo
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Deployed on Streamlit Community Cloud — `https://pie-time.streamlit.app/`.

## How it works
`streamlit_app.py:1-65`

- `decimal_hours = hour + minute/60 + second/3600 + microsecond/3_600_000_000` (`streamlit_app.py:45`)
- `pi_time = decimal_hours / π` and `year_pi = year / π`
- Auto-refresh via `@st.fragment(run_every=0.1)` — avoids the `while True: time.sleep()` anti-pattern that blocks Streamlit's execution model
- Background injected as `data:image/jpeg;base64,...` via `get_base64_background()` (`streamlit_app.py:14-24`) — works on Streamlit Cloud where `./bg.png` URL fails; prefers `bg.jpg` (1920×1080, ~377KB) with fallback to `bg.png`

## Project structure
```
Pie-time/
├── streamlit_app.py   # main app
├── bg.jpg             # optimized background (1920×1080, JPEG q85)
├── requirements.txt   # streamlit==1.64.0, pillow==12.3.0
├── README.md
└── .gitignore
```

## Background image
Original `bg.png` (2560×1440, 4.7 MB) optimized to `bg.jpg` (1920×1080, ~377 KB, JPEG quality 85). To use your own:

1. Place `bg.jpg` or `bg.png` in project root
2. App auto-detects `bg.jpg` first, then `bg.png`

Or bring back the PNG: `Pillow` compress with `Image.save("bg.png", optimize=True)`.

## Requirements
- Python 3.12+
- `streamlit==1.64.0` (see `requirements.txt`)


## AI Usage
AI assistance (Muse Spark via OpenCode) was used to fix and optimize this project:

- Guide the user to learn and write this project
- Optimized `bg.png` (4.7 MB) → `bg.jpg` (377 KB, 1920×1080 JPEG)
- Added `requirements.txt`, expanded `.gitignore` and 90% this README.
- Verified via `py_compile`, `ast.parse`, and headless `streamlit run` (health 200)

All changes reviewed and tested locally on windows.

## License
MIT — feel free to fork and pie-ify(?).
