# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
from os.path import isdir, isfile, join
import signal

from flask import abort, Flask, redirect

app = Flask(__name__)

# Set config for file system path and filename prefix
mnt_dir = os.environ.get("MNT_DIR", "/mnt/nfs/filestore")
filename = os.environ.get("FILENAME", "test")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    """Renders UI by redirects to the file system path to interact with file
    system.

    Writes a new file on each request.
    """
    # Redirect to mount path
    path = "/" + path
    if not path.startswith(mnt_dir):
        return redirect(mnt_dir)

    return os.listdir(path)


# To locally run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))