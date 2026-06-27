import requests
from bs4 import BeautifulSoup

url = "https://165.npa.gov.tw"

try:
    response = requests.get(url, timeout=10, verify=False)

    print("網站連線成功！")
    print("HTTP 狀態碼：", response.status_code)

except Exception as e:
    print("發生錯誤：", e)