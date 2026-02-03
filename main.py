from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/map")
def map_view():
    return render_template("map.html")

@app.route("/guardar_punto", methods=["POST"])
def guardar_punto():
    data = request.json
    print(data)  # {'lat': ..., 'lng': ...}
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
