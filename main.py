from flask import Flask, request
from sheet_writer import write_to_sheet

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" not in data:
        return "No message", 200
    msg = data["message"]["text"]

    status = "否" if "没破" in msg or "没有" in msg else "是"
    mood = "普通"
    if "低落" in msg: mood = "低落"
    if "开心" in msg: mood = "积极"
    note = msg

    write_to_sheet(status, mood, note)
    return "ok", 200

if __name__ == '__main__':
    app.run()
