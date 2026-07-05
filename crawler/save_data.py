import csv
import os


def save_to_csv(data, filename="data/scam_cases.csv"):

    # 如果 data 資料夾不存在，就自動建立
    os.makedirs("data", exist_ok=True)

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.writer(file)

        # 寫入欄位名稱
        writer.writerow([
            "id",
            "title",
            "publish_date",
            "content"
        ])

        # 寫入每一筆資料
        for item in data:
            writer.writerow([
                item["id"],
                item["title"],
                item["publish_date"],
                item["content"]
            ])

    print("CSV 儲存成功！")
    print("檔案位置：", filename)