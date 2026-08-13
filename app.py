import os
import requests

from flask import Flask, jsonify, render_template
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


# Exact API from your .apib file
API_BASE_URL = "https://getthirukural.appspot.com/api/3.0"

APP_ID = os.getenv("THIRUKKURAL_APP_ID", "").strip()


def fetch_kural(number):

    if not APP_ID:
        raise RuntimeError(
            "THIRUKKURAL_APP_ID is missing."
        )

    # Example:
    # https://getthirukural.appspot.com/api/3.0/kural/1
    url = f"{API_BASE_URL}/kural/{number}"

    params = {
        "appid": APP_ID,
        "format": "json"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    result = response.json()

    # API returns Kural object
    if isinstance(result, dict):

        if "number" in result:
            return result

        # Handle wrapped response
        if isinstance(result.get("data"), dict):
            return result["data"]

        if isinstance(result.get("kural"), dict):
            return result["kural"]

    raise ValueError(
        f"Unexpected API response: {result}"
    )


# ---------------- HOME ----------------

@app.route("/")
def home():

    return render_template("index.html")


# ---------------- GET KURAL ----------------

@app.route("/api/kural/<int:number>")
def kural(number):

    # Valid Kural numbers
    if number < 1 or number > 1330:

        return jsonify({
            "success": False,
            "message": "Kural number must be between 1 and 1330."
        }), 400

    try:

        data = fetch_kural(number)

        return jsonify({
            "success": True,
            "data": data
        })

    except requests.RequestException as error:

        return jsonify({
            "success": False,
            "message": "Could not connect to Thirukkural API.",
            "details": str(error)
        }), 502

    except Exception as error:

        return jsonify({
            "success": False,
            "message": str(error)
        }), 500


# ---------------- RANDOM KURAL ----------------

@app.route("/api/kural/random")
def random_kural():

    try:

        data = fetch_kural("rnd")

        return jsonify({
            "success": True,
            "data": data
        })

    except Exception as error:

        return jsonify({
            "success": False,
            "message": str(error)
        }), 500


# ---------------- RUN APP ----------------

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )