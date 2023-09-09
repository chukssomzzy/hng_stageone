#!venv/bin/python3

"""HNG stage one api route for backend track"""

from datetime import date, datetime
from os import getenv
from flask import Flask, abort, request
from dotenv import load_dotenv
assert (load_dotenv())

app = Flask(__name__)

time = "%Y-%m-%dT%H:%M:%S.%f"


@app.route("/api", strict_slashes=False)
def get_about():
    """Get about for a person track"""
    slack_name = request.args.get("slack_name")
    track = request.args.get('track')
    d = date.today()
    print(request.args)
    if not slack_name or not track:
        abort(400, "make the args correct")
    res_out = {}
    res_out["slack_name"] = slack_name
    res_out["track"] = track
    res_out["current_day"] = d.strftime("%A")
    res_out["utc_time"] = datetime.strftime(datetime.utcnow(), time)
    res_out["status_code"] = 200
    res_out["github_repo_url"] = "https://github.com/chukssomzzy/hng_stageone"
    res_out["github_file_url"] = \
        "https://github.com/chukssomzzy/hnb_stageone/blob/main/app.py"
    return res_out


if __name__ == "__main__":
    port = getenv("APP_PORT", 4000)
    host = getenv("APP_HOST", "127.0.0.1")
    debug = getenv("APP_DEBUG", False)
    app.run(port=int(port), host=host, debug=bool(debug))
