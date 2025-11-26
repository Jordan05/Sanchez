from flask import Flask, request, jsonify
app = Flask(__name__)

# Endpoint de salud
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

# Endpoint "IA" mínimo: simula una respuesta inteligente
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json() or {}
    prompt = data.get("prompt", "")
    # "IA" simple: devuelve prompt con transformación
    if not prompt:
        return jsonify({"error": "no prompt provided"}), 400
    answer = f"Simulated-IA-response: {prompt[::-1]}"  # ejemplo simple
    return jsonify({"prompt": prompt, "answer": answer}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
