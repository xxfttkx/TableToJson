import json

# 文件路径
input_file = 'characters.json'
output_file = 'sorted_characters.txt'

# 加载 JSON 数据
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 排除 "実装日": "実装日"，并且保留有"実装日"和"キャラ名"的项
filtered = [
    item for item in data
    if item.get("実装日") != "実装日" and "実装日" in item and "キャラ名" in item
]

# 将"実装日"字符串转为真正的日期进行排序
from datetime import datetime
def parse_date(item):
    try:
        return datetime.strptime(item["実装日"], "%Y/%m/%d")
    except Exception:
        return datetime.max  # 无法解析的放到最后

sorted_items = sorted(filtered, key=parse_date)

# 输出为 `[ ] キャラ名`，每项间空一行
with open(output_file, 'w', encoding='utf-8') as f:
    for item in sorted_items:
        f.write(f"[ ] {item['キャラ名']}\n\n")

print(f"已写入 {output_file}")
