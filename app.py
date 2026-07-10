from flask import Flask, render_template, request, redirect, url_for

from db import (
    create_table,
    get_all_cases,
    insert_case,
    get_case_by_id,
    update_case,
    delete_case
)


app = Flask(__name__)


# 首頁
@app.route("/")
def index():
    return render_template("index.html")


# Read：顯示全部案件
@app.route("/cases")
def cases():
    scam_cases = get_all_cases()

    print("PostgreSQL 讀到資料筆數：", len(scam_cases))

    return render_template(
        "cases.html",
        cases=scam_cases
    )


# Create：新增案件
@app.route("/cases/add", methods=["GET", "POST"])
def add_case():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        publish_date = request.form.get("publish_date", "").strip()
        content = request.form.get("content", "").strip()

        if not title:
            return "案件標題不能空白", 400

        insert_case(
            title,
            publish_date,
            content
        )

        return redirect(url_for("cases"))

    return render_template("add_case.html")


# Update：修改案件
@app.route("/cases/edit/<int:case_id>", methods=["GET", "POST"])
def edit_case(case_id):
    scam_case = get_case_by_id(case_id)

    if scam_case is None:
        return "找不到這筆資料", 404

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        publish_date = request.form.get("publish_date", "").strip()
        content = request.form.get("content", "").strip()

        if not title:
            return "案件標題不能空白", 400

        update_case(
            case_id,
            title,
            publish_date,
            content
        )

        return redirect(url_for("cases"))

    return render_template(
        "edit_case.html",
        scam_case=scam_case
    )


# Delete：刪除案件
@app.route("/cases/delete/<int:case_id>", methods=["POST"])
def remove_case(case_id):
    delete_case(case_id)

    return redirect(url_for("cases"))


if __name__ == "__main__":
    create_table()
    app.run(debug=True)