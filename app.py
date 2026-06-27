from flask import Flask, render_template, request

app = Flask(__name__)

cases_data = [
    {
        "title": "假投資群組詐騙",
        "type": "投資詐騙",
        "money": "120,000 元",
        "content": "詐騙集團透過 LINE 群組宣稱保證獲利，要求被害人先匯款到指定帳戶。"
    },
    {
        "title": "假網購賣家詐騙",
        "type": "網購詐騙",
        "money": "3,500 元",
        "content": "被害人在社群平台購買商品，付款後賣家封鎖帳號並消失。"
    },
    {
        "title": "假交友投資詐騙",
        "type": "交友詐騙",
        "money": "80,000 元",
        "content": "詐騙者以交友名義取得信任，再誘導被害人投入虛假投資平台。"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cases")
def cases():
    keyword = request.args.get("keyword", "")

    if keyword:
        filtered_cases = [
            c for c in cases_data
            if keyword in c["title"] or keyword in c["type"] or keyword in c["content"]
        ]
    else:
        filtered_cases = cases_data

    return render_template("cases.html", cases=filtered_cases)

if __name__ == "__main__":
    app.run(debug=True)