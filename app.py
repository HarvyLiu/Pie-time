from flask import Flask, render_template
import base64
from pathlib import Path

app = Flask(__name__)

def get_base64_background(paths):
    for p in paths:
        if p.is_file():
            b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
            mime = "image/jpeg" if p.suffix == ".jpg" else "image/png"
            return b64, mime
    return None
# At least this function can be migrated here seamlessly
@app.route("/")
def index():
    result = get_base64_background([Path("static/bg.jpg")])
    bg_data, bg_mime = result if result else (None, None)
    return render_template("index.html", bg_data=bg_data, bg_mime=bg_mime)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
