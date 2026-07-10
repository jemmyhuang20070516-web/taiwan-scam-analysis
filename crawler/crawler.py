import sys
import os
import requests
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db import insert_case

print("程式真的開始執行了")

headers = {
    "User-Agent": "Mozilla/5.0"
}

all_data = []

for page in range(1, 2):
    url = f"https://165.npa.gov.tw/api/article/top/{page}"

    print("正在抓第", page, "頁")

    response = requests.get(
        url,
        headers=headers,
        timeout=10,
        verify=False
    )

    print("狀態碼：", response.status_code)

    data = response.json()

    if not isinstance(data, list):
        print("第", page, "頁不是文章資料，跳過")
        continue

for item in data:
    if not isinstance(item, dict):
        print("跳過非文章資料：", item)
        continue

    content_html = item.get("content", "")
    soup = BeautifulSoup(content_html, "html.parser")
    content_text = soup.get_text(" ", strip=True)

    all_data.append({
        "id": item.get("id"),
        "title": item.get("title", ""),
        "publish_date": item.get("publishDate", ""),
        "content": content_text
    })

print("總共抓到：", len(all_data), "筆資料")

for case in all_data:
    insert_case(
        case["title"],
        case["publish_date"],
        case["content"]
    )

print("資料已寫入 PostgreSQL")