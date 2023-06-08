import os

from flask import Flask


app = Flask(__name__)

mnt_dir = os.environ.get("MNT_DIR", "/mnt/nfs/filestore")
filename = os.environ.get("FILENAME", "test")

@app("/")
def home():
    return os.listdir(mnt_dir)