import os

from flask import Flask


app = Flask(__name__)

mnt_dir = os.environ.get("MNT_DIR", "/mnt/nfs/filestore")
filename = os.environ.get("FILENAME", "test")

@app.route("/")
def home():
    return os.listdir(mnt_dir)

# To locally run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))