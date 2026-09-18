from flask import Flask, jsonify
from system_info_manager import SystemInfoManager

app = Flask(__name__)

@app.route("/cypress-api/system-info", methods=["GET"])
def system_info():
    manager = SystemInfoManager()
    return jsonify(manager.get_system_info())

app.run(host="0.0.0.0", port=5000)