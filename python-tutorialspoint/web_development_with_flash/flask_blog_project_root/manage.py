import os, sys

# Ensure current folder is in Python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,PROJECT_ROOT)

from flask_blog import app

print("WORKING DIR:", os.getcwd())
print("PYTHON PATH:")
for p in sys.path:
    print(" -", p)

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )