import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
load_dotenv(".env")

# 環境変数からAPIキーを取得
api_key = os.environ["RIOT_GAMES_API_KEY"]


@app.route("/api/get-account-info")
def get_account_info():
    game_name = request.args.get("game_name")
    tag_line = request.args.get("tag_line")

    if not game_name or not tag_line:
        return jsonify({"error": "Missing game_name or tag_line"}), 400

    region = "asia"
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return (
            jsonify({"error": f"Error {response.status_code}: {response.text}"}),
            response.status_code,
        )


if __name__ == "__main__":
    app.run(debug=True)
