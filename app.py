from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cases")
def cases():
    scam_cases = []

    with open(
        "data/scam_cases.csv",
        "r",
        encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            scam_cases.append(row)

        print("讀到資料筆數：", len(scam_cases))

    return render_template(
        "cases.html",
        cases=scam_cases
    )

if __name__ == "__main__":
    app.run(debug=True)