import requests
from bs4 import BeautifulSoup
import json

def table_to_json(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    table = None
    tables = soup.find_all("table")
    for table in tables:
        first_row = table.find("tr")
        first_cell = first_row.find(['td', 'th']) if first_row else None
        if first_cell:
            text = first_cell.get_text(strip=True)
            # 这就是角色表
            if(text=='No'):
                table = table
                break

    # 提取表头
    headers = [th.get_text(strip=True) for th in table.find_all('tr')[0].find_all(['th', 'td'])]

    data = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all(['td', 'th'])
        if len(cells) != len(headers):
            continue
        item = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}
        data.append(item)

    return data

# 示例使用
url = "https://twinklestarknights.wikiru.jp/?キャラクター一覧"
json_data = table_to_json(url)



with open("characters.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

