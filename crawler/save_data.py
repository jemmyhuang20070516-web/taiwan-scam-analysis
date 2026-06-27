import json

cases = [
    {
        "title": "假投資群組詐騙",
        "type": "投資詐騙",
        "money": 120000,
        "content": "LINE投資群組保證獲利，要求匯款。"
    },
    {
        "title": "假網購詐騙",
        "type": "網購詐騙",
        "money": 3500,
        "content": "付款後賣家失聯。"
    },
    {
        "title": "假交友投資",
        "type": "交友詐騙",
        "money": 80000,
        "content": "交友後誘導下載投資APP。"
    },
    {
        "title": "解除分期付款",
        "type": "ATM詐騙",
        "money": 15000,
        "content": "假客服要求操作ATM解除分期。"
    },
    {
        "title": "假中獎通知",
        "type": "抽獎詐騙",
        "money": 5000,
        "content": "通知中獎，要求先支付手續費。"
    }
]

with open("data/cases.json", "w", encoding="utf-8") as f:
    json.dump(cases, f, ensure_ascii=False, indent=4)

print("資料已成功存到 data/cases.json")