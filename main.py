from flask import Flask, request
import os

app = Flask(__name__)

# Criar diretório de logs caso não exista
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "remote_log.txt")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

@app.route("/upload-log", methods=["POST"])
def upload_log():
    log = request.form.get("log", "")

    print(log)
    
    if not log:
        return "Log vazio", 400

    # Salvar o log no arquivo
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log + "\n")

    return "Log recebido com sucesso!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)